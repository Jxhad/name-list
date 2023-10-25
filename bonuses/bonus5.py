import random

userinput1 = int(input('Please enter a whole number: '))
userinput2 = int(input('Please enter another whole number: '))

if userinput1 != userinput2:
    if userinput1 > userinput2:
        randomNum = random.randint(userinput2, userinput1)
    else:
        randomNum = random.randint(userinput1, userinput2)
    
    print(f"The random number between {userinput1} and {userinput2} is: {randomNum}")
else:
    print('The numbers are equal. Please enter valid numbers.')
