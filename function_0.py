# def add(a,b):
#     c=a+b
#     return c
#
# print(add(5,4))

# def sum(a,b):
#     return a+b
#
# result=sum(4,2)
# print(result)

# def format_name(f_name,l_name):
#     formatted_f_name=f_name.title()
#     formatted_l_name=l_name.title()
#     print(f"{formatted_f_name} {formatted_l_name}")
#
# format_name("jeNny","KHATRI")
'''Jenny Khatri'''

# import statistics
# def mean_median_mode(list1):
#      return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
#
# result=mean_median_mode([1,2,89,4,5,6,7,8,9])
# print(result)         #(14.555555555555555, 6, 1)
#
# a,b,c=mean_median_mode([1,2,89,4,5,6,7,8,9])
# print(f"mean is {a}\nmedian is {b}\nmode is {c}")
'''mean is 14.555555555555555
median is 6
mode is 1'''

# def leap_year(year):
#     if year%4==0:
#         return True
#     else:
#         return False
# def days_in_month(year,month):
#     days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if (leap_year(year) and month==2):
#         return 29
#     else:
#         return days_list[month-1]
#
# year=int(input("enter the year"))
# month=int(input("enter the month"))
# days=days_in_month(year,month)
# print(days)
'''enter the year3098
enter the month2
28
Process finished with exit code 0'''