import ReturnMessage
import json
from   requests import request
def Processing(xml_dict,msg_type,SET):
    if msg_type == "text":
       return Text(xml_dict,SET)
    else:
       return Others(xml_dict)

def Text(xml_dict,SET):
    Content = str.lower(xml_dict.get("Content"))
    Copyright = SET["MAIN"]
    #使用run启动，keyword.json对应着run的目录
    with open(r'../resource/KeyWord.json', 'r', encoding="utf-8") as f:
        KeyWord = json.load(f)
        if Content in KeyWord.keys():
            if KeyWord[Content][0:4] == "pic_":
                return ReturnMessage.ReturnPic(xml_dict,KeyWord[Content][4:])
            else:
                return ReturnMessage.ReturnText(xml_dict,Copyright +"\n\n"+ KeyWord[Content])
        else:
            url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s" % Content
            rep = request("get", url)
            msg_ = rep.content.decode()
            dict = json.loads(msg_)
            return  ReturnMessage.ReturnText(xml_dict,dict["content"])



def Others(xml_dict):
    return ReturnMessage.ReturnException(xml_dict)






