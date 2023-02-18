# LESSON 2 YSLOVIYA
x = int(input('Введите ваше число: '))
if x > 0:
    print(x, 'это оложительное число')
else:
    print(x, 'это отрицательное число')

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('First quarter')
    else:
        print('Fourth quarter')
else:
    if y > 0:
        print('Second quarter')
    else:
        print('Third quarter')

x = int(input())
y = int(input())
if x % 10 == 0 or y % 10 == 0:
    print('Yes')
else:
    print('No')

#Vivod naimenshego
x = int(input())
y = int(input())
if x > y:
    print(y)
else:
    print(x)

#znak 4isla
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#chessboard
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if (x + y + x1 + y1)%2 == 0:
    print('Yes')
else:
    print('No')

#visokos_god
x = int(input())
if x%4 == 0 and x%100 != 0 or x%400 == 0:
    print("Yes")
else:
    print('No')

#min 3 chisla
x1 = int(input())
x2 = int(input())
x3 = int(input())
if x2 >= x1 <= x3:
    print(x1)
elif x1 >= x2 <= x3:
    print(x2)
else:
    print(x3)

#skolko sovpadaet chisel
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('3')
elif a == b or b == c  or a==c:
    print('2')
else:
    print('0')

#ladya
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if x == x1 and y != y1 or y == y1 and x != x1:
    print('Yes')
else:
    print('No')

#Korol
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')

#Slon
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) >= 1 and abs(y1 - y2) >= 1:
    print('YES')
else:
    print('NO')

#Ferz
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
     print('NO')

#Kon'
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == 2 and abs(y1-y2) == 1 or abs(x1-x2) == 1 and abs(y1-y2)==2:
    print('YES')
else:
    print("NO")
