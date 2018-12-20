from data import dataset

def addUsercountry(student_ticket, country, money):
    if student_ticket in dataset:
        if country in dataset[student_ticket]:
            country_list = dataset[student_ticket][country]
            country_list.append(money)
        else:
            dataset[student_ticket][country] =[money]
    else:
        dataset[student_ticket] = dict()
        dataset[student_ticket][country] = [money]


addUsercountry(student_ticket, country, money)

print(dataset)
