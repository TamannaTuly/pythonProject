# i = 1
# exact_number= 5
# j = 0
# k= 3
#
# while i<= k:
#     g = int(input('number :'))
#     if g == exact_number:
#         print('You won!')
#         break
#     else:
#         print('try again!')
#         i += 1
# if g != exact_number:
#     print('you lost!')


#modification
number = 56
i=1
g=5
j=0
g_number=int(input('enter guessed number'))
while i<g:
    if g_number!=number:
        if g_number>50:
            g_number=int(input('too high! enter again : '))
            i+=1
        else:
            g_number = int(input('too low! enter again : '))
            i+=1
    else:
        print('you won')
        break
if g_number != number:
    print('you lost!')