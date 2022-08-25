def fibo(signature, n):

    if n==0: return []
    elif n==1: return signature[1]
    elif n>2: return fibo(signature[n-1]) + fibo(signature[n-2]) + fibo(signature[n-3])



def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

rec_fib(n=10)



def tribonacci(signature, n):
    
    a, b, c = signature [-3:]
    
    if n==0: return []
    elif n==1: return [a]
    elif n==2: return [b] 
    elif n==3: return [c]
    elif n>3: 
        print('n is ', n)
        print('signature is ', signature)
        
        return tribonacci(signature, n-3) + [tribonacci(signature, n-1)[0] + tribonacci(signature, n-2)[0] + tribonacci(signature, n-3)[0]] 

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

for i in range(-2):
    print(i)