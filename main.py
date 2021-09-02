# # msg='Welcome to Python 101: Strings'
# # print(msg.find('Python'))
# # print(msg.replace('Python', 'Java'))
# # msgTest=msg.replace('Python','c')
# # print(msgTest.title())
# #
# # print('Python' in msg)
# #
# #
# # name = 'TERRY'
# # color ='RED'
# # msgName = '[' + name + ']' + ' ' + 'loves the color' + ' '+ color.lower() + '!'
# # print(msgName)
# #
# # msgName1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# # print(msgName1)
# #
# # firstName= input ("What is your name : ")
# # print(f'hello {firstName.upper()}!')
# #
# #
# # a = input ('first Number : ')
# # b= input ('second Number : ')
# # result = float(a)+float(b)
# # print(result)
#
# friends =['tuly', 'modon', 'mintz','khikz']
# print(friends)
# print(friends[0])
# print(len(friends))
# print(friends.index('tuly'))
#
# car = ['125','258','120','500']
# car.sort()
# print(car)
# car.sort(reverse=True)
# print(car)
# car.reverse()
# print(car)
# print(min(friends))
# print(max(car))
# friends.append('tamanna')
# print(friends)
# friends.insert(5,'medona')
# print(friends)
# friends [3]='niger'
# print(friends)
# friends.extend(car)
# print(friends)
# friends.remove('medona')
# print(friends)
# friends.pop()
# print(friends)
# # friends.clear()
# # print(friends)
# # del friends[2]
# # print(friends)
# # new_friends = friends[:]
# # new_friends = friends.copy();
# new_friends = list(friends)
# print(new_friends)
#

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# c = int(input('enter the input : '))
# sales_w2.insert(6,c)
# sales_w1.extend(sales_w2)
# print(sales_w1)
# sales.extend(sales_w1)
# print(sales)
# max_earn =1.5 * max(sales);
# min_earn =1.5 * min(sales);
# # total_earn =1.5 * sum(sales);
#
# print(max_earn)
# print(min_earn)
# print(max_earn+min_earn)



# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# n = int(input('enter the income : '))
# sales_w2.append(int(n))
# # sales_w2.insert(6,n)
# # print(sales_w2)
# sales_w1.extend(sales_w2)
# # print(sales_w1)
# sales.extend(sales_w1)
# print(sales)
# min_income=1.5*int(min(sales))
# max_income = 1.5 * int(max(sales))
# total_income = min_income + max_income
# print(min_income)
# print(max_income)
# print(total_income)

# msg ='Welcome  to  Python  101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(list(msg))
# print(msg.split())
# print(msg.split(' '))
# print(msg.split(' '),type(msg.split()))
# print(csv.split(','))
# name_input=input('name : ')
# print(name_input.split('t'))
# print(name_input.split(' '))
# print(csv.split(' '))
# print('-'.join(friends_list+friends_list))
# print(''.join(friends_list+friends_list))
# print(' '.join((msg.split())))

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = []
# csv_without_comma = ' '.join(csv.split(','))
# # print(csv_without_comma)
# csv_without_colon = ' '.join(csv_without_comma.split(':'))
# # print(csv_without_colon)
# csv_without_semicolon = ' '.join(csv_without_colon.split(';'))
# # print(csv_without_semicolon)
# list_friends = csv_without_semicolon.split(' ')
# friends_list.extend(list_friends)
# # print(list_friends)
# print(friends_list)
# print(csv.replace(';',',').replace(':',',').split(','))
# frndz= (','.join((','.join(csv.split(';')).split(':'))).split(','))
# (','.join(','.join(csv.split(';')).split(':'))).split(',')
# print(frndz)


# list , tuples , set all of them are
# 1. behaves like list, but tuples are unchangeable (pop, remove can't be applied here)
# 2. faster series : sets> tuples > list bcz sets are unordered and remove the duplicates
# 3. [list], (tuple), {set}

# friend_sets = {'tuly', 'test', 'tamanna', 'tuly','checker'}
# print(friend_sets)
# friend_sets_outer = {'tuly','tamanna','test','chest'}
# print(friend_sets_outer)
# print(friend_sets.intersection(friend_sets_outer))
# print(friend_sets.difference(friend_sets_outer))
# null_friends ={'abc'}
# print(null_friends.intersection(friend_sets_outer))

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']
# # print('Eric' in friends)
# # print('John' in friends)
#
# print('Eric' in friends and 'John' in friends)
# print(friends.union(my_friends))
# print(friends | my_friends)
# print(friends.intersection(my_friends))
# print(friends & my_friends)
# print(friends.difference(my_friends))
# print(friends - my_friends)
# print(friends)
# print(my_friends)
# print(friends.symmetric_difference(my_friends))
# print(friends ^ my_friends)
# cars =list(set(cars))
# print(cars)

#function : parameter
# function : pass value ==argument
# function : param = "any value" if nothing passed then this will be the default value

# def common_message(name = "tamanna" ,age = "50"):
#     print('Hello ' + name + '!' + ' You are ' + age + ' year\'s old.')
#
# name = input('Enter your name:')
# age = '20'
# common_message(name, age)
# common_message(name)
# common_message(age)#why can't I pass null value(argument) to the first param? :(

# exercise
# def message(color):
#     print(f"We hear you like the color {color.lower()}!")
# color='RED'
# message(color)
# def age_calculator(age):
#     print(f"Your age will be {age+1} next year")
# age = 11
# age_calculator(age)


#return statements
# def return_sum(salary):
#     tax = salary * 2.5
#     return [tax,salary]
#     # print(tax)
#
# print(return_sum(25))
# # return_sum(2)

#comparison

# a=5
# b=1
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print('u' in 'tuly')
# print('u' not in 'tuly')
# print(int(True))
# print(int(False))
# print(bool(True))
# print(bool(False))
# print(int(1))
# print(bool(1))
# print(int(0))
# print(bool(0))
# print(bool([1,2]))
# print(42+False)
# print(42+True)

# is_raining = True
# print("nice")
# if is_raining:
#     print("ok")
#
# is_raining = False
# print("nice")
# if is_raining:
#     print("ok")

# rain = True
# cold = False
# sunny = False
# # if rain:
# #     print("Bring an umbrella!")
# # else:
# #     print("Bring an umbrella for protecting yourself from sun")
# # if rain and cold:
# #     print('Rain & cold')
# # else:
# #     print('Not raining neither cold')
# #
# # if rain or cold:
# #     print('Rain & cold')
# # else:
# #     print('Not raining neither cold')
#
# # elif
# if sunny:
#     print("Apply sun block")
# elif rain and cold :
#     print("Bring umbrella and jacket")
# elif rain and not (cold):
#     print("Bring umbrella")
# elif not (rain) and cold:
#     print("Bring jacket")
# else:
#     print("Enjoy the weather!!!!!")

# credit card company: let user to pay using credit card without PIN under transaction of amount 50bucks

amount = 50
if amount <= 50:
    print('Purchase approved !!')
else:
    print("Please enter your pin : ")



