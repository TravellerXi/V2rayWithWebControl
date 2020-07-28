#!/usr/bin/python3
# coding:utf-8
import os
import platform


fullchain_cer = '''
-----BEGIN CERTIFICATE-----
MIIFbTCCBFWgAwIBAgISA+EKzWjNWdEGeZTpUD3j1QQ8MA0GCSqGSIb3DQEBCwUA
MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD
ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xOTEyMDkwMTMyMDlaFw0y
MDAzMDgwMTMyMDlaMBoxGDAWBgNVBAMTD2Zhc3RzcGVlZGdvLnh5ejCCASIwDQYJ
KoZIhvcNAQEBBQADggEPADCCAQoCggEBALyhHmzxcLG0muwio0l1ZL8RW6TQzHkh
DW76ej3NGiW5gcXs5fpMc+8y9kEf71XI4XzWzno9fvkmV4b3f9S21DFpR+In1I6A
1f79bBV9yI4JDd40Empmc0pn93HzENt2FyT0XWzTP7VR75jjEFHG6WEX7Ky9a9QM
rt+HKSjuTKAhU1eIMAL7LwxQE/t42RoJTuOWWJV2zcFwAJK696GRjIkP6My3MnLu
MUfl0Yuiv/Nid0yV1R7QqlxYhiFQSLV+BdKUIuAUfWObNG5FYdHj/ynS3S7IAu0l
Nrf+73Zhfa+t+3Gx+L+UTNbJ1y3V7KN3g0478rVKtCy+3NuQKu+lTysCAwEAAaOC
AnswggJ3MA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYB
BQUHAwIwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUy3HnGS8BI6KPfDDZFb0NCB2a
mgAwHwYDVR0jBBgwFoAUqEpqYwR93brm0Tm3pkVl7/Oo7KEwbwYIKwYBBQUHAQEE
YzBhMC4GCCsGAQUFBzABhiJodHRwOi8vb2NzcC5pbnQteDMubGV0c2VuY3J5cHQu
b3JnMC8GCCsGAQUFBzAChiNodHRwOi8vY2VydC5pbnQteDMubGV0c2VuY3J5cHQu
b3JnLzAvBgNVHREEKDAmgg9mYXN0c3BlZWRnby54eXqCE3d3dy5mYXN0c3BlZWRn
by54eXowTAYDVR0gBEUwQzAIBgZngQwBAgEwNwYLKwYBBAGC3xMBAQEwKDAmBggr
BgEFBQcCARYaaHR0cDovL2Nwcy5sZXRzZW5jcnlwdC5vcmcwggEGBgorBgEEAdZ5
AgQCBIH3BIH0APIAdwBep3P531bA57U2SH3QSeAyepGaDIShEhKEGHWWgXFFWAAA
AW7of/L+AAAEAwBIMEYCIQD/62bHf7zijFx2VwI9KvTI1eTM2fWM0ju6PwYac8o0
wwIhANX+qzD1ALg+l24HP8BlLac4h0muZ7EStyiT48/CIDkAAHcAB7dcG+V9aP/x
sMYdIxXHuuZXfFeUt2ruvGE6GmnTohwAAAFu6H/zHgAABAMASDBGAiEAojklWmzM
C1Mx+mn+X845GOKQ1BMwtPKKu4c/2zpOiVUCIQCOFv9pQ5wqx3fPfrqSh8OHiyXu
uxaQSdM07S/GX/7ZPDANBgkqhkiG9w0BAQsFAAOCAQEABg7TtmXHWxvaWpJd3sSO
hbp6RBn9R+7jn4FGchaJ91fwZK4YC7b7LWbVoPE0fOg9ZoEu10owizi1oTGjzrhv
l+RevpBhLxZQ6wj+YLwW/tkmcpK8UF1quVNfb6mFSJI1MK+AGNeTUvpT8r7ojoK6
Rtqkq49DAfoyfrGg5tAFEEjJtPu6tTWSr/Rz7RbvSHJKgfDs1gMoP8PtanY/VGUh
3cYZe9yoxlEVyqZE55w7S4aqS4Ol3FAterBlRMlUfxh/d2yfowBad5/BjZGlil0y
46wcdoyP7H0j61aujgjGWhJ4Ms717Qo/90kLqonQrXSSuvn6YDzbf95CJqVtipC8
Og==
-----END CERTIFICATE-----

-----BEGIN CERTIFICATE-----
MIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/
MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
DkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow
SjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT
GkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF
q6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8
SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0
Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA
a6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj
/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T
AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG
CCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv
bTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k
c3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw
VAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC
ARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz
MDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu
Y3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF
AAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo
uM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/
wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu
X4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG
PfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6
KOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==
-----END CERTIFICATE-----


'''

fastspeedgo_xyz_key = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAvKEebPFwsbSa7CKjSXVkvxFbpNDMeSENbvp6Pc0aJbmBxezl
+kxz7zL2QR/vVcjhfNbOej1++SZXhvd/1LbUMWlH4ifUjoDV/v1sFX3IjgkN3jQS
amZzSmf3cfMQ23YXJPRdbNM/tVHvmOMQUcbpYRfsrL1r1Ayu34cpKO5MoCFTV4gw
AvsvDFAT+3jZGglO45ZYlXbNwXAAkrr3oZGMiQ/ozLcycu4xR+XRi6K/82J3TJXV
HtCqXFiGIVBItX4F0pQi4BR9Y5s0bkVh0eP/KdLdLsgC7SU2t/7vdmF9r637cbH4
v5RM1snXLdXso3eDTjvytUq0LL7c25Aq76VPKwIDAQABAoIBAGMd8oPidooaUdHE
/bJK6m5v64z2XotDr/Bh07wHuzaZfLSJH+tfIwhM6hMcecHE9Z+IrCSVjdPTruhv
ww7+Jw/zt18B+PIMhuYfOh0s5CamYVAiYo7gWLJ/YQnSZEg9jDnR4gmeE3runAzl
O50M/XMUhDvcqP1a0MUKG7mzRjZZhQKQPHDINZKyGjXhIS8aWBkB88IR/T6QMH1I
+vFtEjd2Zv1iKJKltUK3BD9KDYUUYrPH3MHC9X7yaMis6E25/9SLJxq8G4t43SUb
7njjWJQ3wax082sIdJQYZ7ivSiDohKTQz8bhnLAv1ZAUYMbj/xlYNp1x4MeaUoD6
xTYWjRECgYEA7LKfERvPyIcheB4n04Yhk2aXwQpQdL5azH+0U2Zs12QmnoG+9E5z
N6OVKxCflKwsqJemrJfATWwwJMnYngN3R2UUlXKPQ73tea6axXP+KDhW7TF/5veW
BSsTizHc9J7OfSahdSOFHMDhMqyznNk5VnQsHLcVF5Ss7q0xyD9WnjMCgYEAzAMB
tFiJ3/QASB1fH5RmO6NWh2Wj8MUxU0kcewPA6R4oIBPYs4CbLenk2iTDL+xgYgAI
yzDXM79t8N/FB/pv91CnrPaOAKPW5MXE4pxX9+DpW3lbDTfNr32sOjxkda1KpfzR
15tsr87tJFZ6nLiYuEGsOPC2mjn6llcgZKFHIykCgYEAuOrTWopfyknH3A+zDY28
rWt5I1brhEkyppEeUAm0/pE/mpXCmRqw6MbjwsE56uyX9x6DGFN16QacliEbGlea
2Cwf6KGXS1UWMfo28Auug72AK86AHfFPQrpkilpqRLHMn/mOKfWWCOCnDu/dYqxS
HzijPcvKrqF4eP7V5ZuWEAECgYBQF6oWpF/UlVV6+lT67+bG6RQyabvX7YK04NIW
lV2p55X3KfN8XTQO7XFUFvSuHs2kC8FoDA+gmDnQQ/l1bWOBo5+AbvdG1wupmt71
3E1I2nqi19zgLpVInTz9S/JgpJzW14+GZtVfnAxLpMvUNUB3rgiv/giiObrgROpJ
t2tXKQKBgQDZnXxFEfsTE5DBUcu2sYeXfZ1jQhZNks0uiRBOaG1oIbghAv3HqePU
IsF1vdcV+tpWgjAhScknqhbRaHcJp0vIhhAzlIScvoRpxy8xILgTUoOyCUuY47Sk
IRHo1TFBZGMBO//Dx2hyox7BwGeU1WatOT8MpLdcHn/+sDoUcXNELQ==
-----END RSA PRIVATE KEY-----

'''
dhparam_pem = '''
-----BEGIN DH PARAMETERS-----
MIIBCAKCAQEAyI2icSurwMn/XPfibOLJlHwf61ulHbZYcPhB19hQOMEqEFGJ934k
ysxI+V9BE1b4K9mHpYJTFCMoAA8zlO7Z5Yf8GnbOLBv+hoSk49oyUq1iAzhFZMEE
XmF1YHW8R9wFXoghw3E+35nqUFHTm2dL3Tzqf0G1QIMw7fAjJ0knCRptTZDSKnGi
Wlw7uFdG9yTWT4bwX4oKfHoXXm9WV3NKB6slKqY1jcghqDcQSDmbLNLwfFZ7b/+5
nguFdfXGMH5S+C8r7Kv96BAytypmAFudOdigaNwiloHPQC9+//y+EyA6kqqFlAS+
F4YrQnzDEJ8pqZPRqHv97dgopvZiKUuDCwIBAg==
-----END DH PARAMETERS-----

'''

def prepare(Servername,ServerIP):
    WebUi_beforeIP = '''
    server {
        listen 80;
        listen [::]:80;
        server_name '''
    WebUi_afterIP = ''';
        # enforce https
       location ~ ^/ {
               proxy_pass http://127.0.0.1:8082;
               proxy_http_version 1.1;
                       proxy_set_header  Host $host:$server_port;
               proxy_set_header Host $host;
               proxy_set_header X-Real-IP $remote_addr;
               proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
               client_max_body_size 10240M;
               client_body_timeout 5m;

           # Show realip in v2ray access.log
           # proxy_set_header X-Real-IP $remote_addr;
           # proxy_set_header Host $host;
           # proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              }


    }
    '''


    NginxConfigurationInfo = '''
    server {
        listen 80;
        listen [::]:80;
        server_name ''' + Servername + ''';
        # enforce https
        return 301 https://''' + Servername + ''';
    }

    server
        {
            listen 443 ssl http2;
            #listen [::]:443 ssl http2;
            server_name ''' + Servername + ''';
            index index.html index.htm index.php default.html default.htm default.php;
            root  /var/www/html/;
            access_log /var/log/''' + Servername + ''';

            ssl_certificate /etc/nginx/ssl/fullchain.cer;
            ssl_certificate_key /etc/nginx/ssl/fastspeedgo.xyz.key;
            ssl_session_timeout 5m;
            ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
            ssl_prefer_server_ciphers on;
            ssl_ciphers "TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-128-CCM-8-SHA256:TLS13-AES-128-CCM-SHA256:EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5";
            ssl_session_cache builtin:1000 shared:SSL:10m;
            # openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
            ssl_dhparam /etc/nginx/ssl/dhparam.pem;
            location /web {
               proxy_redirect off;
               proxy_pass http://127.0.0.1:9999;
               proxy_http_version 1.1;
               proxy_set_header Upgrade $http_upgrade;
               proxy_set_header Connection "upgrade";
               proxy_set_header Host $http_host;

           # Show realip in v2ray access.log
           # proxy_set_header X-Real-IP $remote_addr;
           # proxy_set_header Host $host;
           # proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

              }

        }

    '''
    os.system('yum install wget curl unzip nginx -y')
    os.system('mkdir -p /etc/nginx/ssl')
    os.system('mkdir -p /var/www/html')
    with open('/etc/nginx/ssl/fullchain.cer', 'w') as f:
        f.write(fullchain_cer)
    with open('/etc/nginx/ssl/fastspeedgo.xyz.key', 'w') as f:
        f.write(fastspeedgo_xyz_key)
    with open('/etc/nginx/ssl/dhparam.pem', 'w') as f:
        f.write(dhparam_pem)
    with open('/etc/nginx/conf.d/' + Servername+'.conf', 'w') as f:
        f.write(NginxConfigurationInfo)
    os.system('rm -rf /usr/share/nginx/html')
    with open('/etc/nginx/conf.d/webui.conf', 'w') as f:
        f.write(WebUi_beforeIP+ServerIP+WebUi_afterIP)
    print ('预准备环境完毕')
def configure_nginx_v2ray():
    v2ray = '''
    #!/bin/sh
    #
    # v2ray        Startup script for v2ray
    #
    # chkconfig: - 24 76
    # processname: v2ray
    # pidfile: /var/run/v2ray.pid
    # description: V2Ray proxy services
    #

    ### BEGIN INIT INFO
    # Provides:          v2ray
    # Required-Start:    $network $local_fs $remote_fs
    # Required-Stop:     $remote_fs
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: V2Ray proxy services
    # Description:       V2Ray proxy services
    ### END INIT INFO

    DESC=v2ray
    NAME=v2ray
    DAEMON=/usr/bin/v2ray/v2ray
    PIDFILE=/var/run/$NAME.pid
    LOCKFILE=/var/lock/subsys/$NAME
    SCRIPTNAME=/etc/init.d/$NAME
    RETVAL=0

    DAEMON_OPTS="-config /etc/v2ray/config.json"

    # Exit if the package is not installed
    [ -x $DAEMON ] || exit 0

    # Read configuration variable file if it is present
    [ -r /etc/default/$NAME ] && . /etc/default/$NAME

    # Source function library.
    . /etc/rc.d/init.d/functions

    start() {
      local pids=$(pgrep -f $DAEMON)
      if [ -n "$pids" ]; then
        echo "$NAME (pid $pids) is already running"
        RETVAL=0
        return 0
      fi

      echo -n $"Starting $NAME: "

      mkdir -p /var/log/v2ray
      $DAEMON $DAEMON_OPTS 1>/dev/null 2>&1 &
      echo $! > $PIDFILE

      sleep 2
      pgrep -f $DAEMON >/dev/null 2>&1
      RETVAL=$?
      if [ $RETVAL -eq 0 ]; then
        success; echo
        touch $LOCKFILE
      else
        failure; echo
      fi
      return $RETVAL
    }

    stop() {
      local pids=$(pgrep -f $DAEMON)
      if [ -z "$pids" ]; then
        echo "$NAME is not running"
        RETVAL=0
        return 0
      fi

      echo -n $"Stopping $NAME: "
      killproc -p ${PIDFILE} ${NAME}
      RETVAL=$?
      echo
      [ $RETVAL = 0 ] && rm -f ${LOCKFILE} ${PIDFILE}
    }

    reload() {
      echo -n $"Reloading $NAME: "
      killproc -p ${PIDFILE} ${NAME} -HUP
      RETVAL=$?
      echo
    }

    rh_status() {
      status -p ${PIDFILE} ${DAEMON}
    }

    # See how we were called.
    case "$1" in
      start)
        rh_status >/dev/null 2>&1 && exit 0
        start
        ;;
      stop)
        stop
        ;;
      status)
        rh_status
        RETVAL=$?
        ;;
      restart)
        stop
        start
        ;;
      reload)
        reload
      ;;
      *)
        echo "Usage: $SCRIPTNAME {start|stop|status|reload|restart}" >&2
        RETVAL=2
      ;;
    esac
    exit $RETVAL


    '''

    v2ray_config = '''
    {
        "log": {
        "loglevel": "warning",
        "access": "/var/log/v2ray/access.log", 
        "error": "/var/log/v2ray/error.log"
      },

      "inbounds": [
        {
          "port": 9999,
          "listen":"127.0.0.1",
          "protocol": "vmess",
          "settings": {
            "clients": [
              {
                "id": "b8c77c2f-476a-4bab-886d-f1d9cc258bbe",
                "alterId": 88
              }
            ]
          },
          "streamSettings": {
            "network": "ws",
            "wsSettings": {
            "path": "/web"
            }
          }
        }
      ],
      "outbounds": [
        {
          "protocol": "freedom",
          "settings": {}
        }
      ]
    }
    '''
    systeminfo = platform.linux_distribution()
    ServerVersion = systeminfo[1][:1]
    if ServerVersion == '6':
        print('开始为Centos 6 配置V2ray和Nginx')
        os.system('yum install mysql -y')
        with open('/etc/init.d/v2ray', 'w') as f:
            f.write(v2ray)
        os.system('chmod a+x /etc/init.d/v2ray')
        os.system('chkconfig v2ray on')
        with open('/etc/v2ray/config.json', 'w') as f:
            f.write(v2ray_config)
        os.system('service iptables stop')
        os.system('chkconfig iptables off')
        os.system('service v2ray restart')
        os.system('service mysqld start')
        os.system('chkconfig mysqld on')
        os.system('systemctl restart nginx')
    elif ServerVersion == '7':
        print('开始为Centos 7 配置V2ray和Nginx')
        os.system('yum install mariadb mariadb-server -y')
        os.system('systemctl stop v2ray')
        with open('/etc/v2ray/config.json', 'w') as f:
            f.write(v2ray_config)
        os.system('systemctl stop firewalld')
        os.system('systemctl disable firewalld')
        os.system('systemctl start v2ray')
        os.system('systemctl start mariadb')
        os.system('systemctl enable mariadb')
        os.system('systemctl restart nginx')
    else:
        print('您的系统版本不受支持，前往 https://github.com/TravellerXi/V2rayWithWebControl 查看受支持的系统版本。')
        exit()
    print('\nv2ray及Nginx配置并启动完毕\n')

webui_init_configure='''
#!/bin/bash
bash /V2rayWithWebControl/static/start.sh start

'''

### 开始准备web界面
def webui_configure():
    print('\n准备WEB界面中')
    os.system('mkdir -p /V2rayWithWebControl')
    os.system('wget -P /V2rayWithWebControl https://mirror.fastspeedgo.xyz/V2rayWithWebControl/webui.zip')
    os.system('unzip -d /V2rayWithWebControl /V2rayWithWebControl/webui.zip')
    os.system('mysql -uroot </V2rayWithWebControl/static/v2ray.sql')
    #os.system('cp /V2rayWithWebControl/static/startv2rayui.sh /etc/init.d/')
    with open ('/etc/init.d/startv2rayui.sh', 'w') as f:
        f.write(webui_init_configure)
    os.system('bash /V2rayWithWebControl/static/start.sh start')
    print('\nWeb 页面已启动')


if __name__=='__main__':
    print('开始处理环境依赖等问题>>>')
    print('请输入绑定的域名，域名可以使用Cloudflare提供的免费的CDN服务来加速V2ray，输入完毕请回车：')
    Servername = input()
    print('请输入您服务器的公网IP，按回车确认:')
    ServerIP = input()
    prepare(Servername,ServerIP)
    print('\n现在，开始安装v2ray核心>>>\n')
    os.system('wget -P /tmp/ https://mirror.fastspeedgo.xyz/V2rayWithWebControl/go.sh')
    os.system('bash /tmp/go.sh')
    print('\n现在，开始处理v2ray配置和nginx配置>>>\n')
    configure_nginx_v2ray()
    print('\n现在，开始处理WEB UI管理页面\n')
    webui_configure()
    print('配置完毕，web管理地址为http://'+ServerIP+'\n以下是用于连接V2ray客户端的设置信息：\n地址：'+Servername+'\n端口：443\n用户ID：b8c77c2f-476a-4bab-886d-f1d9cc258bbe\n额外ID：88\n加密方式:auto\n传输协议：ws\n路径：/web\n底层传输;tls\n其他保持默认')

