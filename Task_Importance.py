import math
salary = int(input('Введите вашу зарплату: '))
quant_total = int(input('Введите суммарное количество заданий: '))
quant_imp3 = int(input('Введите количество заданий с важностью 3: '))
quant_imp2 = int(input('Введите количество заданий с важностью 2: '))
quant_imp1 = int(input('Введите количество заданий с важностью 1: '))
imp_c = int(input('Введите коэф. важности: '))
imp3_coef = int(1)
imp2_coef = int(2/3)
imp1_coef = int(1/3)
a = int(salary/(int(quant_imp3)*1 + int(quant_imp2)*2/3 + int(quant_imp1)*1/3))
# a = int(salary//(quant_imp3*imp3_coef + quant_imp2*imp2_coef + quant_imp1*imp1_coef))
if imp_c == 3:
    print('Оплата за 1 задание с коэф. важности',imp_c,'составляет ',math.ceil(a))
elif imp_c == 2:
    print('Оплата за 1 задание с коэф. важности', imp_c, 'составляет ', math.ceil(a*2/3))
elif imp_c == 1:
    print('Оплата за 1 задание с коэф. важности',imp_c,'составляет ',math.ceil(a*1/3))
else:
    print('Неверные данные')
print('Проверка по сумме:', math.ceil(float(quant_imp3*a + quant_imp2*a*2/3 + quant_imp1*a*1/3)))
b = math.ceil(float(quant_imp3*a + quant_imp2*a*2/3 + quant_imp1*a*1/3))
# if (quant_imp3*a + quant_imp2*a*2/3 + quant_imp1*a*1/3 == salary):
if (b == salary):
     print ('correct')
else:
     print ('incorrect')
