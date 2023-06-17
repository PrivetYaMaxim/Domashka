def palindrom(a):
    if a==a[::-1]:
        return True
    else:
        return False
a=input('Введите строку:')
print(palindrom(a))