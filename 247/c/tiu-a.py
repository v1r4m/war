#결국 696d706f737369626c655f666c61675f75736572의 encrypted된 값을 찾아야함
#AES알고리즘에는 문제될만한게 없으므로 AES-ECB가 16ㅏ이트로 끊는다는걸 알고서 (=지들만 아는 얘기로) 접근해야 함
#hex문자는 0.5바이트임(4비트=nibble이라고도 불리고... 하튼)
#696d706f737369626c655f666c61675f 75736572
#939454b054b7379b0709a270b894025c2f28487624c5f1476e9fb265d2b47349
#16바이트를 암호화했는데 32바이트가 나온 이유는 패딩때문인데.. 패딩을 뭘로했냐면
self.pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
#len(s) = 16, AES.block_size = 16 그럼 그걸 다시 써본다면...
self.pad = lambda s: s + (16 - 16 % 16) * chr(16 - 16 % 16)
self.pad = lambda s: s + (16 - 0) * chr(16 - 0)
self.pad = lambda s: s + (16 * chr(16))
self.pad = lambda s: s + (16 * 0x10)
#그러므로.. 2f28487624c5f1476e9fb265d2b47349는 10101010101010101010101010101010(실제로 이렇게 나옴)
#PKCS#7 패딩방법인데 뭐 어려운건 아니고 블록단위로 만들어주는 거라고 보면 된다. 뒤에 넣는 패딩은 자리수에 따라 아무거나 쓰레기 값을 넣는다. 
#707ece4f0913868ec5df07d131b0822d
#당연히 못풀었고 지피티님이 푸셨다. 