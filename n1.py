from this import s


s1 = input('Вы ввели строку s1  ')
s2 = input('Вы ввели строку s2 ')
print('<длина первой строки>',len(s1))
print('<длина второй строки> ', len(s2))
print('Первый символ первой строки:', s1[0])
print('Последний символ последней строки:', s2[-1])
print('"s1" равен "s2"?')
print(s1 == s2)
print('"s1" содержится ли в "s2":') 
print(s1 in s2)
print('А наоборот?')
print(s2 in s1)
