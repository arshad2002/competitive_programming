def romantointeger(s):
    symbol = ("I","V","X","L","C","D","M")
    value = (1,5,10,50,100,500,1000)
    numbers = dict(zip(symbol,value))
    sum = 0
    prev = ''
    
    for n in s[::-1]:
        if n =='I' and (prev =='V' or prev == 'X'):
            sum -= numbers.get(n)
            continue
        elif n == 'X' and (prev == 'L' or prev == 'C'):
            sum -= numbers.get(n)
            continue
        elif n == 'C' and (prev == 'D' or prev == 'M'):
            sum -= numbers.get(n)
            continue
        else:
            sum+=numbers.get(n)
        prev = n
    return sum
        

if __name__ == "__main__":
    s= "MCMXCIV"
    print(romantointeger(s))



