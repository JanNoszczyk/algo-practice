# Your goal in this problem is to implement an efficient algorithm for computing Fibonacci numbers.
# Uses python3

def calc_fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		f = []
		for i in range(n):
			f.append(0)
		f[0] = 0
		f[1] = 1
		for i in range(2,n):
			f[i] = f[i-1] + f[i-2]
		return f[n-1] + f[n-2]

n = int(input())
print(calc_fib(n))
