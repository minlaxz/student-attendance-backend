from urllib.request import urlopen
import urllib
def check():
    try:
        urlopen('http://www.example.com', timeout=3)
        return True
    except urllib.error.URLError: 
        return False
