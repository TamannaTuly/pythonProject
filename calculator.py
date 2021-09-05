# print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
def plus_operation(a, b):
    c = int(a) + int(b);
    print(f"your result for plus operation is {c}");


def minus_operation(a, b):
    c = int(a) - int(b);
    print(f"your result for minus operation is {c}");


def multiplication_operation(a, b):
    c = int(a) * int(b);
    print(f"your result for multiplication operation is {c}");


def division_operation(a, b):
    c = int(a) / int(b);
    print(f"your result for division operation is {c}");

def temperature(celceous):
    temp = float(celceous * 9 / 5 + 32)
    print(f"your temperature is : {temp}F")

print(f"Chooce your prefered calculator :\n1. Calculator\n2. Temperatur")
d =input('enter any optin(only number): ')
if d=='1':
    print('Operation types are : \n1. plus (+)\n2. minus (-)\n3. multiplication (*)\n4. division (/)' )
    operation_type = input('Please choose your operation type (enter any number from the list:')

    if '1'<=operation_type<='4':
        a = input('Please enter the first number: ')
        b = input('Please enter the second number: ')

        if operation_type=='1':
            plus_operation(a,b)
        elif operation_type=='2':
            minus_operation(a,b)
        elif operation_type=='3':
            multiplication_operation(a,b)
        else:
            if b > '0':
                division_operation(a, b)
            else:
                print(a + ' can\'t be divided by 0! enter valid choice')

    else:
        print("invalid choice")
elif d=='2':
    celceous=float(input('enter celcesous: '))
    if celceous> 0:
        temperature(celceous)
    else:
        print('Please enter valid temperature in C')

else:
    print('Please choose among the option 1 & 2!')
# plus_operation(a,b)
# minus_operation(a,b)
# multiplication_operation(a,b)
# division_operation(a,b)


