n = int(input())
a = 1

if(n == 1):
  print(1)
else:
  n = n - 1
  while(n>0):
    n = n - a*6
    a += 1
  print(a)