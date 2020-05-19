#!/usr/bin/python3

# coding:utf-8

from flask import Flask,request,session,redirect,Response

import platform

import pymysql

from checkupdate import *

from md5 import *

from htmlbase import *

from flask import send_from_directory

import os

basedir = os.path.abspath(os.path.dirname(__file__))



app =Flask(__name__)


def ReturnServiceStatus():
    systeminfo = platform.linux_distribution()
    ServerVersion=systeminfo[1][:1]
    if ServerVersion=='6':
        status = ''
        f = os.popen(r"service v2ray status", "r")
        status = f.read()+'<br>'
        f = os.popen(r"service nginx status", "r")
        status=status+f.read()+'<br>'
        f = os.popen(r"service iptables status", "r")
        status=status+f.read()
        status.replace('\n','<br>')
        notice='<br> 注意，默认 v2ray 和nginx服务应该开启，iptables服务应该关闭'
        status=status+notice
        return status
    else:
        status = ''
        f = os.popen(r"systemctl status v2ray", "r")
        status = f.read()+'<br>'
        f = os.popen(r"systemctl status nginx", "r")
        status = status + f.read()+'<br>'
        f = os.popen(r"systemctl status firewalld", "r")
        status = status + f.read()
        status.replace('\n', '<br>')
        notice = '<br> 注意，默认 v2ray 和nginx服务应该开启，iptables服务应该关闭'
        status = status + notice
        return status

def RestartService():
    systeminfo = platform.linux_distribution()
    ServerVersion = systeminfo[1][:1]
    if ServerVersion == '6':
        os.system("service v2ray restart")
        os.system("service nginx restart")
        os.system("service iptables stop")

    else:
        os.system("systemctl restart v2ray")
        os.system("systemctl restart nginx")
        os.system("systemctl stop firewalld")
    notice = '重启服务完成'
    return notice


def Checkmd5(md5,username):

    db = pymysql.connect('localhost', 'v2ray', 'v2ray', 'v2ray')

    check = db.cursor()

    usernameSQL = 'select md5 from v2ray.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if md5 == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





def ReturnUserlist():

    db = pymysql.connect('localhost', 'v2ray', 'v2ray', 'v2ray')

    check = db.cursor()

    usernameSQL = 'select v2ray from v2ray.user'

    check.execute(usernameSQL)

    Strcheck = str(check.fetchall())

    Strcheck = Strcheck.replace('(', '').replace(')', '').replace(',', '').replace("'", '')

    return (Strcheck)











def Checkisadmin(username):

    db = pymysql.connect('localhost', 'v2ray', 'v2ray', 'v2ray')

    check = db.cursor()

    usernameSQL = 'select isadmin from v2ray.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if result=='yes':

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckUsername(username):

    db = pymysql.connect('localhost', 'v2ray', 'v2ray', 'v2ray')

    check = db.cursor()

    usernameSQL = 'select username from v2ray.user where username=' + "'" + username + "'"

    check.execute(usernameSQL)

    if (check.fetchone()) is None:

        db.close()

        return 0

    else:

        check.execute(usernameSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if username == result:

            db.close()

            return 2

        else:

            db.close()

            return 0





def CheckPassword(username,password):

    db = pymysql.connect('localhost', 'v2ray', 'v2ray', 'v2ray')

    check = db.cursor()

    passwordSQL = 'select password from v2ray.user where username=' + "'" + username + "'"

    check.execute(passwordSQL)

    if check.fetchone() is None:

        db.close()

        return 0

    else:

        check.execute(passwordSQL)

        result=tuple(check.fetchone())

        result = ''.join(result)

        if password == result:

            db.close()

            return 2

        else:

            db.close()

            return 0


@app.route('/', methods=['GET'])
def root_redirect():
    return redirect('/signin')







@app.route('/signin', methods=['GET'])

def signin_form():

    user = request.cookies.get('username')

    md5credit = request.cookies.get('credit')

    if not md5credit:

        return (title_setup_pc('欢迎登录学习管理系统')+'''<form action="/signin" method="post">

                              <p>用户名：<input name="username"></p>

                              <p>密码：&nbsp&nbsp&nbsp<input name="password" type="password"></p>

                              <p><button type="submit">Sign In</button></p>

                              <a href='/signup'target='_blank'>还没有账号？点此注册</a>

                              </form></html>''')

    else:

        result=Checkmd5(md5credit,user)

        if not result:

            return (title_setup_pc('欢迎管理系统')+'''<form action="/signin" method="post">

                          <p>用户名：<input name="username"></p>

                          <p>密码：&nbsp&nbsp&nbsp<input name="password" type="password"></p>

                          <p><button type="submit">Sign In</button></p>

                          <a href='/signup'target='_blank'>还没有账号？点此注册</a>

                          </form>''')

        else:

            return redirect('/success')







@app.route('/signin', methods=['POST'])

def signin():

    # 需要从request对象读取表单内容：

    username=str(request.form['username'])

    password=str(request.form['password'])

    if CheckUsername(username) > 1:

        if CheckPassword(username,password) > 1:

            md5hash = md5(password)

            response=redirect('/success')

            response.set_cookie('username',username,max_age=7*24*3600)

            response.set_cookie('credit',md5hash,max_age=7*24*3600)

            return response



        else:

            return (title_setup_pc('error')+'<p>Bad password</p><br><a href="/signin">返回登录</a>')

    else:

        return (title_setup_pc('error')+'<p>Bad username</p><br><a href="/signin">返回登录</a>')



@app.route('/success', methods=['GET'])

def Success_login():

    user=request.cookies.get('username')

    md5credit=request.cookies.get('credit')

    if not md5credit:

        response = redirect('/signin')

        return response

    else:

        checkmd5 = Checkmd5(md5credit,user)

        if not checkmd5:

            response = redirect('/signin')

            return response

        else:

            if checkupdate() > 0:

                sourcecode = "<h3>Hello, 系统管理员: " + user + "!</h3><br><br>服务器当前状态>>>><br><br>" + ReturnServiceStatus() +"<br><a href='restartservice'target='_blank'>重启所有服务</a>"+ "<br><br><a href='changepasswd'target='_blank'>修改我的密码</a><br><a href='changeinvitecode'target='_blank'>修改邀请码(邀请码用于用户注册，默认openvpn，请务必修改)</a><br><a href='updateversion'target='_blank'>网站后端可更新，点此更新，（不影响原有用户使用VPN）</a><br><br><a href='logout' >注销</a>"

            else:

                sourcecode = "<h3>Hello, 系统管理员: " + user + "!</h3><br><br>服务器当前状态>>>><br><br>" + ReturnServiceStatus() + "<br><a href='restartservice'target='_blank'>重启所有服务</a>"+"<br><br><a href='changepasswd'target='_blank'>修改我的密码</a><br><a href='changeinvitecode'target='_blank'>修改邀请码(邀请码用于用户注册，默认openvpn，请务必修改)</a><br><a href='logout' >注销</a>"

    return (title_setup_pc('主页') + sourcecode)





@app.route('/favicon.ico',methods=['GET'])

def get_fav():

    return app.send_static_file('favicon.ico')

##not return app.send_static_file('static/favicon.ico'), it will automatically use static/...



@app.route('/updateversion',methods=['GET'])

def updateversion_get():
    user = request.cookies.get('username')

    md5credit = request.cookies.get('credit')

    if not md5credit:

        response = redirect('/signin')

        return response

    else:

        checkmd5 = Checkmd5(md5credit, user)

        if not checkmd5:
            response = redirect('/signin')

            return response
        else:
            updateversion()

            return (title_setup_pc('升级成功') + '升级成功！请返回首页<br><a href="/">返回首页</a>')




@app.route('/changepasswd',methods=['GET'])

def change_passwd():

    user = request.cookies.get('username')

    md5credit = request.cookies.get('credit')

    if Checkmd5(md5credit,user)>0:

        return (title_setup_pc('修改我的密码') + '''<form action="/changepasswd" method="post">

                                  <p>密码：&nbsp&nbsp&nbsp<input name="password"></p>

                                  <p><button type="submit">修改</button></p>

                                  </form>''')

    else:

            return (title_setup_pc('error')+'用户未登陆！<br><a href="/signin">返回登录</a>&nbsp<a href="/signup">返回注册</a>')





@app.route('/changepasswd', methods=['POST'])

def change_passwd_post():

    # 需要从request对象读取表单内容：

    user = request.cookies.get('username')

    username=str(user)

    md5credit = request.cookies.get('credit')

    if Checkmd5(md5credit,user)>0:

        password = str(request.form['password'])

        md5hash = md5(password)

        db = pymysql.connect('localhost', 'v2ray', 'v2ray', 'v2ray')

        check = db.cursor()

        usernameSQL = "update v2ray.user set password="+"'"+password+"'"+", md5="+"'"+md5hash+"'"+" where username="+"'"+username+"'"

        check.execute(usernameSQL)

        db.commit()

        db.close()

        return (title_setup_pc('修改成功') + '密码修改成功！<br><a href="/signin">返回登录</a>')

    else:

        return (title_setup_pc('error')+'用户未登陆！<br><a href="/signin">返回登录</a>&nbsp<a href="/signup">返回注册</a>')







@app.route('/logout',methods=['POST','GET'])

def logout():

    response=redirect('/logedout')

    response.delete_cookie('username')

    response.delete_cookie('credit')

    return response



@app.route('/logedout',methods=['GET'])

def logedout():

    return (title_setup_pc('注销页')+"<p>成功注销</p><br><a href='/signin'>返回登录</a>")




@app.route('/restartservice', methods=['GET'])
def Functionrestartservice():
    user = request.cookies.get('username')

    md5credit = request.cookies.get('credit')

    if not md5credit:

        response = redirect('/signin')

        return response

    else:

        checkmd5 = Checkmd5(md5credit, user)

        if not checkmd5:
            response = redirect('/signin')

            return response

        else:
            return(RestartService())







if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8082, debug=True,threaded=True)

