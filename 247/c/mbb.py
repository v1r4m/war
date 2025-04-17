# 첫 4byte가 FF D8 FF D8 이라고 가정

from pathlib import Path

# 경로 설정
enc_path = Path("/Users/ad0559/Downloads/mbb.jpg.enc")
out_path = Path("/Users/ad0559/Downloads/mbb_decrypted.jpg")
data = enc_path.read_bytes()

jpeg_header = bytes.fromhex("FFD8FFE000104A4649460001")
encrypted_prefix = data[:len(jpeg_header)]

xor_key = bytes([e ^ m for e, m in zip(encrypted_prefix, jpeg_header)])
#암호화된 바이트 = 원래 바이트 ^ 키
#복호화도 = 암호화된 바이트 ^ 키 (같은 키로 다시 XOR하면 원래 값이 나옴)
#그래서 예상되는 평문 ^ 암호화된 바이트 = 키

# 키 반복해서 복호화
full_key = (xor_key * (len(data) // len(xor_key) + 1))[:len(data)]
decrypted = bytes([b ^ k for b, k in zip(data, full_key)])

# 복호화된 결과 저장
out_path.write_bytes(decrypted)

print(f"복호화 완료! 저장 위치: {out_path}")
