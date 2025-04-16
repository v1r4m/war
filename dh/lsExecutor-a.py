from pwn import *
import dotenv
import os
dotenv.load_dotenv()

p = remote(os.environ.get('DH_URL'),19698)
payload = 0
# option에서 그냥 엔터를 누르면 \n