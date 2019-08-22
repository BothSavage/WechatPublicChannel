#执行这个步骤的时候记住把本机ip放入白名单
import os
import requests
import json
with open(r'../resource/SET.json', 'r', encoding="utf-8") as f:
    SET = json.load(f)
    APPID = SET["APPID"]
    APPSECRET = SET["APPSECRET"]
url_token = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (APPID,APPSECRET)
response_token = requests.post(url=url_token)
access_token = json.loads(response_token.text)["access_token"]
pic_dir = input("请输入要上传文件的绝对路径:")
#参考官方文档，调用的cmd的curl命令
cmd = 'curl -F media=@%s "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=%s"' % (pic_dir,access_token)
print(os.system(cmd))