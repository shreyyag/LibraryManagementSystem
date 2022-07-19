def Bdate():
    import datetime
    now = datetime.datetime.now
    return str(now().date())

def Btime():
    import datetime
    now = datetime.datetime.now
    return str(now().time())