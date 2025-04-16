# ad0559@MacBook-Pro-Eunjin utils % telnet 254e61d0754dbbbe.247ctf.com 50154
# Trying 144.76.74.118...
# Connected to 254e61d0754dbbbe.247ctf.com.
# Escape character is '^]'.
# Welcome to the 247CTF addition verifier!
# If you can solve 500 addition problems, we will give you a flag!
# What is the answer to 387 + 183?
# 570
# Yes, correct!
# What is the answer to 194 + 34?

# telnet 254e61d0754dbbbe.247ctf.com 50154
import socket
import time
import dotenv
import os

dotenv.load_dotenv()
HOST = os.getenv("247_TAT_HOST")
PORT = int(os.getenv("247_TAT_PORT"))
def recv_line(s):
    data = b""
    while not data.endswith(b"\n"):
        chunk = s.recv(1)
        if not chunk:
            break
        data += chunk
    return data.decode()
def solve_addition_problem(problem):
    parts = problem.split()
    num1 = int(parts[5])
    num2 = int(parts[7][:-1])  # Remove the '?' at the end
    print(f"num1: {num1}, num2: {num2}")
    
    # Calculate the sum
    result = num1 + num2
    
    return result
def main():
    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    welcome_message = recv_line(s)
    print(welcome_message)
    
    # Loop to solve addition problems
    while True:
        com = recv_line(s)
        print(com)

        problem = recv_line(s)
        print(problem)
        # Solve the addition problem
        answer = solve_addition_problem(problem)
        
        s.sendall(f"{answer}\r\n".encode())
        
        # Optional: Sleep for a short time to avoid overwhelming the server
        time.sleep(1)
    
    # Close the connection
    s.close()

if __name__ == "__main__":
    main()