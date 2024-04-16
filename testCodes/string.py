string = '0123456789'

desconsiderar = input("Número: ")

try:
    desconsiderar = int(int(desconsiderar)/1)
except:
    desconsiderar = 0

if desconsiderar == 0:
    print(string)
else: 
    print(string[:-desconsiderar])