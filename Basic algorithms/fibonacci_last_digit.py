# Your goal in this problem is to find the last digit of 𝑛-th Fibonacci number. 
# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    f = []
    for i in range(n):
        f.append(0)
    f[0] = 0
    f[1] = 1
    for i in range(2,n):
        f[i] = (f[i-1] + f[i-2]) % 10
    return (f[n-1] + f[n-2]) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
