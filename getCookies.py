import json
def openCookies():
    try:
        with open('session_cookies','r') as file:
            session_cookies = eval(file.read())
            return session_cookies
    except:
        return None

def writeCookies(session):
    session_cookies = session
    with open('session_cookies','w') as outFile:
        outFile.write(json.dumps(session_cookies))


