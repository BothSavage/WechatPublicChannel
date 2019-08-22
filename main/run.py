from flask import Flask,request,abort
import xmltodict
import json
from  function import EventProcessing,MessageProcessing
with open(r'../resource/SET.json', 'r', encoding="utf-8") as f:
    SET = json.load(f)
    WECHAT_TOKEN = SET["WECHAT_TOKEN"]

app = Flask(__name__)
@app.route("/wx",methods=["GET","POST"])
def wechat():
    #1.验证微信服务器，这里偷懒，返回字符串就完事，实际要验证
    echostr = request.args.get("echostr")
    if echostr is not  None:
        return  echostr
    #2.解析消息类型
    xml_to_dct = xmltodict.parse(request.data)
    xml_dict = xml_to_dct.get("xml")
    msg_type = xml_dict.get("MsgType")

    #3.处理消息
    if msg_type == "event":
        resp = EventProcessing.Processing(xml_dict,xml_dict.get("Event"))
    else:
        resp =MessageProcessing.Processing(xml_dict,msg_type,SET)

    #4.返回消息
    resp = xmltodict.unparse(resp)
    return resp


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=80)
