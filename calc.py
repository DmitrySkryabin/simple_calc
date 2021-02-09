def add(x, y):
	return x + y



print("Выберете опертор")
print("1.плюс")
whatwedo = input()
print("Введите цифры")
num1 = int(input())
num2 = int(input())

if whatwedo == '1':
	print(num1," + ",num2," = ",add(num1,num2))