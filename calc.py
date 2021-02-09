def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x * y

print("Выберете опертор")
print("1.плюс")
print("2.минус")
print("3.умножение")
print("4.деление")
whatwedo = input()
print("Введите цифры")
num1 = int(input())
num2 = int(input())

if whatwedo == '1':
	print(num1," + ",num2," = ",add(num1,num2))
if whatwedo == '2':
	print(num1," - ",num2," = ",subtract(num1,num2))
if whatwedo == '3':
	print(num1," * ",num2," = ",multiply(num1,num2))
if whatwedo == '4':
	print(num1," / ",num2," = ",divide(num1,num2))
else:
	print("Введите корректоное значение")