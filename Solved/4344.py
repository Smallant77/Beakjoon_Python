n = int(input())
for i in range(n):
  a = list(input().split())
  avg = 0
  for i in a[1:]:
    avg += int(i)
  avg = avg / (len(a)-1) 
  
  b = 0
  for i in a[1:]:
    if (int(i)>avg):
      b += 1
  print(str(format(b/(len(a)-1)*100, ".3f"))+'%')