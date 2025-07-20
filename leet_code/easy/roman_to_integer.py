roman = 'MCMXCIV'
roman_num=list(roman)


dict ={
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000    
}

num = 0
for  rom in range(len(roman_num)):
    if(rom < len(roman_num)-1 and dict[roman_num[rom]]<dict[roman[rom+1]]):
        num -= dict[roman_num[rom]]
    else:
        num += dict[roman_num[rom]]

print(num)




# optimal solution


