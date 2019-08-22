import ReturnMessage

def Processing(xml_dict,Event):
    if Event == "subscribe":
        return  Subscribe(xml_dict)
    elif Event == "unsubscribe":
        Unsubscribe(xml_dict)
    else:
        return  Others(xml_dict)


def Subscribe(xml_dict):
    return ReturnMessage.ReturnText(xml_dict,"欢迎订阅")


def Unsubscribe(xml_dict):
    pass

def Others(xml_dict):
    return  ReturnMessage.ReturnException(xml_dict)


