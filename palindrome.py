palindrom = str(input())
a = len(palindrom)
i = 0
a = a - 1
n = 0
while a - i >= i:
    if palindrom[a - i] == palindrom[i]:
        i += 1
    else:
        n = 1
        break
if n == 1:
  print("false")
else:
  print("true")
