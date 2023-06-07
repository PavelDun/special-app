oper = input('Выберите операцию: ')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
a = 0
if oper == '+':
	a = num1 + num2
	
elif oper == '*':
	a = num1 * num2
	
elif oper == '/':
	a = num1 / num2
	
elif oper == '-':
	a = num1 - num2
	
else:
	print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
print(a)
