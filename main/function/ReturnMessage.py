import time

def  ReturnText(xml_dict,text):
    resp_dict = {
        "xml":{
            "ToUserName":xml_dict.get("FromUserName"),
            "FromUserName":xml_dict.get("ToUserName"),
            "CreateTime":int(time.time()),
            "MsgType":"text",
            "Content":text
        }
    }
    return resp_dict


def  ReturnException(xml_dict):
    resp_dict = {
        "xml":{
            "ToUserName":xml_dict.get("FromUserName"),
            "FromUserName":xml_dict.get("ToUserName"),
            "CreateTime":int(time.time()),
            "MsgType":"text",
            "Content":"目前只支持文字类型"
        }
    }
    return resp_dict


def  ReturnPic(xml_dict,id):
    resp_dict = {
        "xml":{
            "ToUserName":xml_dict.get("FromUserName"),
            "FromUserName":xml_dict.get("ToUserName"),
            "CreateTime":int(time.time()),
            "MsgType":"image",
            "Image":{"MediaId":id}
        }
    }
    return resp_dict