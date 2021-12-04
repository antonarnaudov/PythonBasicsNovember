num = 5
text = 'abc'
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6

if num == 5:
    num += 2
    if num == 6 or text == 'abc' and number2 == 2 \
            and number3 == 3 and number4 == 4 \
            and number5 == 5 and number6 == 6:
        print(num, text)
    else:
        print('nope')
else:
    pass
