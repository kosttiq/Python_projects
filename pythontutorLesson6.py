#LIST OF SQUARES
n = int(input())
i = 1
while i**2 <= n :
    print(i ** 2)
    i += 1
   
#MIN DIV
n = int(input())
i = 2
while n % i != 0:
    i+=1
print(i)

#DEGREE OF 2
n = int(input())
i = 2
degree = 1
while i <= n:
    i *= 2
    degree += 1
print(degree - 1, i//2)

#MORNING RUN
x = int(input())
y = int(input())
days = 1
while x < y:
    x *= 1.1
    days += 1
print(days)

#SEQUENCE LENGTH
n = int(input())
i=0
while n!=0:
    i+=1
    n=int(input())
print(i)

#SEQUENCE SUM
n = int(input())
i=0
while n!=0:
    i+=n
    n=int(input())
print(i)

#SEQUENCE AVG
n = int(input())
i=0
x=0
while n!=0:
    i+=n
    x+=1
    n=int(input())
print(i/x)

#SEQUENCE MAX
n = int(input())
maximum = n
while n != 0:
    if n > maximum:
        maximum = n
    n = int(input())
print (maximum)

#QUANTITY OF N%2 == 0 
n = -1
i = -1
while n != 0:
    n = int(input())
    if n%2 == 0:
        i+=1
print(i)

#QUANTITY OF ELEMENTS > PREVIOUS
n = int(input())
i = 0
while n != 0:
    a = int(input())
    if n < a and a != 0:
        i += 1
    n = a
print(i)

#SECOND MAX
max1 = max2 = 0
n = int(input())
while n != 0:
    if n >= max1:
        max2 = max1
        max1 = n
    if max2 < n and n < max1:
        max2 = n
    n = int(input())
print(max2)






