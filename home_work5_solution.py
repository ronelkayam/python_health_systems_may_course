# """
# 1.	כתוב פונקציה שמקבלת משקל (בק"ג) וגובה (במטרים) ומחזירה את ערך ה־BMI
# """
#
#
# def get_bmi_by_kg_and_high(kg, high):
#     # bmi = (kg / high**2)
#     # return bmi
#     return kg / (high ** 2)
#
#
# weight = int(input("please enter your weight:"))
# high = float(input("please enter your high:"))
# bmi = get_bmi_by_kg_and_high(weight, high)
# print(f"your weight:{weight}, your high:{high}, your bmi:{bmi}")
#
# """
# 2.	כתוב פונקציה שמקבלת גיל
# ומחזירה את טווח הדופק התקין לאדם בגיל זה לפי טווחים כלליים.
# """
#
#
# def get_normal_pulse_by_age(age):
#     if age < 20:
#         return 70
#     elif age < 40:
#         return 85
#     elif age < 60:
#         100
#     else:
#         110
#
#
# age = int(input("please enter your age:"))
# normal_pulse = get_normal_pulse_by_age(age)
# print(f"your age is:{age}, and your normal pulse should be:{normal_pulse}")
#
# # option2
# normal_pulse = get_normal_pulse_by_age(int(input("please enter your age:")))
# print(f"your age is:{int(input('please enter your age:'))}, and your normal pulse should be:{normal_pulse}")
#
# # option3
# print(f"your age is:{int(input('please enter your age:'))}, "
#       f"and your normal pulse should be:{get_normal_pulse_by_age(int(input('please enter your age:')))}")
#
# """
# 3.	כתוב פונקציה שמקבלת טמפרטורת גוף במעלות צלזיוס,
# ומחזירה האם יש חום (מעל 38 מעלות).
# """
#
#
# def get_temp_body_high_by_celsius(celsius):
#     return celsius > 38
#
#
# celsius = float(input("please enter your temp body by celsius:"))
# ret = get_temp_body_high_by_celsius(celsius)
# if get_temp_body_high_by_celsius(celsius):  # if ret:
#     print(f"your temp body is high, go to sleep and drink tea!")
# else:
#     print("your temp body is normal, go to dance!")

"""כתוב פונקציה שמקבלת רשימה של ערכי לחץ דם סיסטולי (מספרים שלמים)
, ומחזירה את הממוצע, 
הגבוה ביותר 
והנמוך ביותר.
"""
#
#
# def get_blood_presser_ls_by_size(size):
#     ls = []
#     for i in range(size):
#         ls.append(int(input("please enter your blood presser:")))
#     return ls
#
#
# def get_lower_blood_presser(blood_presser_ls):
#     low = blood_presser_ls[0]
#     for blood_presser in blood_presser_ls[1:len(blood_presser_ls)]:
#         if blood_presser < low:
#             low = blood_presser
#     return low
#
#
# def get_high_blood_presser(blood_presser_ls):
#     high = blood_presser_ls[0]
#     for blood_presser in blood_presser_ls[1:len(blood_presser_ls)]:
#         if blood_presser > high:
#             high = blood_presser
#     return high
#
#
# def get_avg_blood_presser(blood_presser_ls):
#     sum = 0
#     for blood_presser in blood_presser_ls:
#         sum += blood_presser
#     return sum / len(blood_presser_ls)
#
# def say_hello():
#     print("hello and welcome to our clinic:)\ntoday we are calculate some data for blood presser\ngood luck to us:)")
#
# def say_good_bye():
#     print("aehhhaeee today i'm working very hard\n, it's time to sleeping now!")
#
# say_hello()
# size = int(input("What quantity would you like to check blood presser?:"))
# ls = get_blood_presser_ls_by_size(size)
# print(f"low blood presser is:{get_lower_blood_presser(ls)}")
# print(f"high blood presser is:{get_high_blood_presser(ls)}")
# print(f"avg blood presser of {size} patients is:{get_avg_blood_presser(ls)}")
# say_good_bye()
#

"""
14.	כתוב פונקציה שמקבלת רשימת טמפרטורות של חולים (רק מספרים),
 ומחזירה כמה מהם יש להם חום (טמפרטורה מעל 38).
"""


def welcome():
    print("Hello and welcome to our clinic\ntoday we are calculate about temp body\ngood luck to us")


def get_temp_body_ls_by_size(size):
    ls = []
    for i in range(size):
        ls.append(int(input("please enter patient temp body:")))
    return ls


def get_count_with_high_temp_body(temp_body_ls):
    count = 0
    for temp_body in temp_body_ls:
        if temp_body > 37:
            count += 1
    return count


def good_bye():
    print("thank you, was very interest\nnow time to vacation:)")


welcome()
size = int(input("please enter num of patient for today:"))
temp_body_ls = get_temp_body_ls_by_size(size)
print(f"count of patients with high temp body:{get_count_with_high_temp_body(temp_body_ls)}")
good_bye()
