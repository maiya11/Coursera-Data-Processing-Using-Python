'''
A number M is a Monisen number if M=2**P-1 and both M and P are prime numbers. 
For example, if P=5, M=2**P-1=31, 5 and 31 are both prime numbers, so 31 is a Monisen number.
'''

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


  def monisen(n):
    for i in range(2, n+1):
        m = (2 ** i) - 1
        if is_prime(i) and is_prime(m):
            return m
        else:
            return None