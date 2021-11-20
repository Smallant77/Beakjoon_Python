//다이얼을 list로 만들어 놓고 in을 이용한 구현
a = list(input())
ans = 0

Num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in a:
  for b in Num:
    if i in b:
      ans += Num.index(b) + 3

print(ans)