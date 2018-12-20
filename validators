"""Формат студентського квитка: КВ- і 8 цифр
   Формат назв країн: всі літери маленькі, назви можуть складатись з декількох слів
   Формат грошей: дійсне число, 4 знаки після і до коми"""

import re

def getStudentticket():

    user_input = input("Enter number of the student's ticket")

    if(re.match(r"^'KB-'\d{8}$",user_input)):
        return user_input
    else:
        return False


def getCountryname():

    user_input = input("Enter name of the country")

    if (re.match(r"^[a-z]+$",user_input)):
        return user_input
    else:
        return False


def getMoney():

    user_input = input("Enter sum of money")

    if (re.match(r"^\d.{4}\.\d.{4}$",user_input)):
        return user_input
    else:
        return False
