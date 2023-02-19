#LESSON 4 TSIKL FOR

#RYAD 1
a = int(input())
b = int(input())
for i in range (a, b+1):
    print(i)

#RYAD 2
a = int(input())
b = int(input())
if a < b:
    for i in range (a, b+1):
     print(i)
else:
    for i in range (a, b-1, -1):
        print(i)

#RYAD 3
a = int(input())
b = int(input())
for i in range (a-int((a%2)==0), b-1, -2):
    print(i)

#SUM 10 CHISEL
s = 0
for i in range(10):
    num = int(input())
    s += num
print(s)

#SUM N CHISEL
n = int(input())
s = 0
for i in range(n):
    num = int(input())
    s += num
print(s)

#SUM KUBOV
n = int(input())
s = 0
for i in range(1, n+1):
    s += i ** 3
print(s)

#FAKTORIAL
n = int(input())
a = 1
for i in range(1, n + 1):
    a *= i
print(a)

#SUM FAKTORIALOV
n = int(input())
a = 1
sum = 1
for i in range(2, n + 1):
    a *= i
    sum += a
print(sum)

