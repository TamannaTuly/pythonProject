month = input('Enter the month name with first 3 words : ').lower()

def num_days(month='feb'):

    # if month == 'jan' or month=='dec' or month=='oct' or month=='aug' or month == 'jul' or month=='may' or month=='mar':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
    #     print('number of days in',month,'is',30)
    # else:
    #     print('Invalid month name')
    days = 31
    if month in {'apr','jun','sep' ,'nov'}:
        days =30
    elif month in {'feb'}:
        days =28
    print(f"number of {month}\'s is {days} days")

num_days(month)
# optimize/shorten the code in the function
# try to reduce the number of conditionals
