#执行这个步骤的时候记住把本机ip放入白名单
import requests
import json
with open(r'../../resource/SET.json', 'r', encoding="utf-8") as f:
    SET = json.load(f)
    APPID = SET["APPID"]
    APPSECRET = SET["APPSECRET"]
type = input("请输入素材的类型，image,video,voice,news：")
offset = input("请输入开始位置(从全部素材的该偏移位置开始返回，0表示从第一个素材返回):")
count = input("请输入素材的数量，取值在1到20之间：")
data= {
    "type": type,
    "offset": int(offset),
    "count": int(count)

}
url_token = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (APPID,APPSECRET)
response_token = requests.post(url=url_token)
access_token = json.loads(response_token.text)["access_token"]
url_list = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s" % access_token
response_list = requests.post(url=url_list,data=json.dumps(data))
for i in json.loads(response_list.text)["item"]:
    print(i)

