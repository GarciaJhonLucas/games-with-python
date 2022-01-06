import sys

count = 1
width = 20

print("Tamaño minimo: 1, Maximo: 15")
number = input("De que tamaño quieres el arbol: ")

try:
    int(number)
    it_is = True
except ValueError:
    it_is = False

if it_is == False:
	print("No se admite esa entrada GRACIAS")
	sys.exit(0)

if int(number) > 15 or int(number) < 1:
	print("No se admite ese tamaño GRACIAS")
	sys.exit(0)

for x in range(int(number)):
	print ('\033[0;32m'+("*"*count).center(width))
	count += 2
print("| |".center(width)+'\033[0m')