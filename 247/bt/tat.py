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
    
    while True:
        com = recv_line(s)
        print(com)

        problem = recv_line(s)
        print(problem)
        answer = solve_addition_problem(problem)
        s.sendall(f"{answer}\r\n".encode()) #와 혐도우 진짜 개 쓰 레기 같은 문제
        
        time.sleep(1)
    
    # Close the connection
    s.close()

if __name__ == "__main__":
    main()