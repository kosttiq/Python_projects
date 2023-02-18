#LESSON 1 VVOD I VIVOD
input("Введите ваше число: ")

if 2 > 2:
    print ('2 is greater than 2')
elif 2 > 2:
    print('2 is not greater than 2')
else:
    print('2 is equal 2')\

#сумма чисел
a = int(input('Введите первое число: '))
b = int(input("Введите второе число: "))
s = a + b
print('Сумма чисел равна: ', s)

#площадь треугольника
a = int(input())
b = int(input())
s = 0.5 * a * b
print('Площадь треугольника равна ', s)

#дележ яблок
a = int(input('Кол-во детей: '))
b = int(input('Кол-во яблок: '))
s = b//a
print('каждому достанется по ', s, 'яблок')
print('в корзине останется ', b % a, 'яблока')

#Дано число n. С начала суток прошло n минут.
#Определите, сколько часов и минут будут показывать электронные часы в этот момент.
#Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
#Учтите, что число n может быть больше, чем количество минут в сутках.
n = int(input())
h = n%(60*24) // 60
m = n% 60
print(h, m)

#Next & Previous
a = int(input('Введите ваше число:'))
print('The next number for the number',a,'is',a+1)
print('The previous number for the number',a,'is',a-1)

#Tables in classroom
a = int(input('Введите кол-во учеников в первом классе:'))
b = int(input('Введите кол-во учеников во втором классе:'))
c = int(input('Введите кол-во учеников в третьем классе:'))
a1 = a//2 + a%2
b1 = b//2 + b%2
c1 = c//2 + c%2
print(a1+b1+c1)


