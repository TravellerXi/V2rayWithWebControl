# V2rayWithWebControl

介绍:安装v2ray，并提供web管理后台，可在后台重启服务，查看服务状态，下载客户端和配置等。

<br>

安装教程：一句话安装：<br><br>
bash <(curl -L -s https://mirror.fastspeedgo.xyz/V2rayWithWebControl/install.sh) 

<br>
适用于 Centos 6/Centos7。

<br><br>
使用指南：
<br>1. 本脚本调用Python3执行，将会使用yum安装Python3。
<br>2. 运行过程中第一次提示输入绑定的域名，在/etc/nginx/conf.d目录下生成'域名.conf'的Nginx配置文件，将域名绑定到该文件里，并启用SSL，默认证书放置目录/etc/nginx/ssl，用户可按需自行替换为自己的证书。
<br>提示：域名可用cloudflare的CDN加速。
<br>3. 运行过程中第二次提示输入服务器公网IP。在/etc/nginx/conf.d目录下生成webui.conf，用做管理页面，该页面目前设置为http页面，用户如有能力可自行更改为https。
<br>4. web管理页面源码在/V2rayWithWebControl/目录下，如遇到web管理页面打不开，可执行该命令重启web管理页面：
bash /V2rayWithWebControl/static/start.sh restart
<br>5. 任何其他问题，欢迎提issue。
