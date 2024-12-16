# we can only convert roman value to integer value which are under 3999
data = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
YorN = 'y'
while YorN != 'n': 
    print('''
Make a Choice:
   1. Type 'int' for  'Integer to Roman'.
   2. Type 'rom' for 'Roman to Integer'.
''')
    choice = input('Enter your Choice: ')
    while choice != 'int' and choice != 'rom':
        print('Invalid Choice')
        choice = input('Enter a Valid Choice: ')
    if choice == 'int':
        num = int(input('Enter an Integer Value: '))
        temp = num
        rom = []
        count = 0
        for v, s in data:
            if temp == 0: break
            count, temp = divmod(temp, v)
            rom.append(s * count)
        print(f"{num} ==> {''.join(rom)}")
        
    else:
        rom = input('Enter a Roman Value: ')
        num = 0
        for r in rom.upper():
            for v, s in data:
                if r == s:
                    num += v
        print(f"{rom} ==> {num}")
            
    YorN = input('Want to try again (y/n): ')
    while YorN != 'n' and YorN != 'y':
        print('Invalid Choice')
        YorN = input('Enter a Valid One: ')
