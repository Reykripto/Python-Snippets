# Fizz Buzz code 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'FizzBuzz')
    elif i % 3 == 0:
        print(f'Fizz')
    elif i % 5 == 0:
        print(f'Buzz')
    else:
        print(i)
