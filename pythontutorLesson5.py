#SLICES (срезы)
a = str(input())
print(a[2])
print(a[-2])
print(a[0:5])
print(a[:-2])
print(a[1::2])
print(a[0::2])
print(a[::-1])
print(a[::-2])
print(len(a))

#STR QUANTITY (кол-во строк)
a = str(input())
print(a.count(' ')+1)

#TWO HALVES (две половины)
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

#REPLACE TWO WORDS (поменять местами два слова)
a = str(input())
w1 = a[:a.find(' ')]
w2 = a[a.find(' ')+1:]
print(w2 + ' ' + w1)

#FIRST AND LAST OCCURRENCE (первое и последнее вхождение)
x = input()
a = x.find('f')
b = x.rfind('f')
if a==b:
    print(a)
elif a == -1:
    print()
else:
    print(a, b)
    
#SECOND OCCURENCE (второе вхождение)
a = input()
b = a.count('f')
if b == 1:
    print(-1)
elif b < 1:
    print(-2)
else:
    print(a.find('f', a.find('f') + 1))
    
#SYMBOL DELETING (удаление символа)
a = input()
print(a.replace('@',''))

#SUBSTRING DELETING (удаление подстроки)
a = input()
print(a.replace('1','one'))

#REPLACING INSIDE A FRAGMENT (замена внутри рагмента)
a = input()
a = a.replace('H', 'h', 1)
a = a.replace('h', 'H', a.count('h') - 1)
print(a)

#DELETING EVERY THIRD SYMBOL (удаление каждого третьего символа)
a = input()
b = ''
for i in range(len(a)):
    if i % 3 != 0:
        b = b + a[i]
print(b)
