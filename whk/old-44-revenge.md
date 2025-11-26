![alt text](image.png)

퍼블v

소스를 읽어보자...FE단에서 6글자 검증을 하고 있고 BE에서도 하고 있다. ./u/내세션 으로 이동하고 소스를 보면 주석으로 친절하게 `ls /`을 입력하라고 알려주고 있다. 단순 `ls`를 하면 `./u/내세션`의 텅 빈 폴더만 보게될테니 말잘듣고 `ls /`을 쳐보자. [ ` 백틱은 $(..)의 deprecatede된 버전이기에](https://stackoverflow.com/questions/53937332/bash-echo-with-escape-backtick-and) echo 문자열을 탈출하여 명령어를 작성할 수 있다. 

first exploit : `` `ls /` ``

`hello! aLooooooongFlag.txt bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var`

그럼 이제 `cat /aLooooooongFlag.txt`을 하면 문제가 풀릴텐데 6글자 제한이 발목을 잡는다. 이거저거 많이 헤맸는데 굳이 ./u/내세션이라는 나의 소중한 공간을 만들어주는게 꼬롬하다. 처음 생각은 touch v로 (내가 viram이고 파일명을 짧게해야하니까 v인것이다..ㅇㅇ) 내용이 cat /aLooooooongFlag.txt인 파일을 만들고 그 파일을 ./u/내세션에서 실행하면 되는거라고 설계했다. 근데 touch도 6글자(사실상 백틱때문에 4글자) 안에는 안들어간다. cat /aLooooooongFlag.txt라는 파일을 만들 방법을 많이 찾아봤는데 방법이 그닥없음 그리고 만들어봐야 append해가면서 첫번째에 cat....두번째에 /aLo... 세번째에 ooo이렇게 붙여나가야 하는데 6글자 내에서는 뭘 어떻게 해도 열받는다.(이렇게 풀어도 재밌었을지도) 그러다가 찾아보니까 * asterisk 를 활용해서 /aLooooooongFlag.txt라는 문자열을 굳이 파일에 넣지 않더라도 명령어로 가져올 수 있다는 사실을 발견했다. 사실 막 어케 설계한거라기보다는 이것저것 넣어보고 알게된거다... 이를테면 `` `>pwd` `` -> `` `ls` ``(잘만들어졌나 확인) -> `` `*` `` 을 해보면 내 위치가 나오는 걸 알 수 있다. 

second exploit : `` `>cat` ``

`` `ls` ``로 확인해보면 cat이 생성된걸 알 수 있다. 

third exploit : `` `* /*` ``

*는 현재 (./u/내세션이라는 소중한 공간) 의 모든 파일명 (cat)으로 치환된다. 공백 뛰고 /*는 /디렉토리의 모든 파일명 `/aLooooooongFlag.txt /bin /boot /dev ...`으로 치환된다. 그러면 결국 `cat /aLooooooongFlag.txt /bin /boot /dev ...` 을 실행한것과 같다. 

만약 내가 헛짓거리 >i >love >cat 이렇게 만들어둬서 세션폴더가 더러워지면 어떻게될까? * 아스타리크는 알파벳순서대로 정렬하기때문에 cat i love /aLoooooongFlag.txt /bin /boot .... 이런 명령어가 생길것이다. cat은 성실하게도 뒤의 인자를 전부 파일로 인식하기 때문에 i라는 파일을 읽고(우리가 만든 파일, 내용없음) love라는 파일을 읽고 플래그 파일을 읽어 정상처리된다. 

그러면 >aa >i >love >cat은? 그럼 명령어가 aa cat i love /aLoooooongFlag.txt /bin /boot ... 가 된다. aa란 없는 명령어기 때문에 세번째 익스플로잇을 넣어도 반응하지 않는다. 이러면 `` `rm *` ``입력해서 다 지워도 되고 그거 생각하기 귀찮으면 소스코드에 내 소중한 공간 ./u/내세션은 00분마다 초기화된다고 쓰여 있으니 기다리자..