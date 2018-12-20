import pprint

'''dataset = {
"category":{
        "order":{
            "family":{"name"}}
    }'''


result = dict()

def add_dataset(data):
    category = data[2]
    if category not in result:
        result[category] = {}
    order = data[3]
    if order not in result[category]:
        result[category][order] = {}
    family = data[4]
    if family not in result[category][order]:
        result[category][order][family] = set()
    name = data[5]
    if name not in result[category][order][family]:
        result[category][order][family].add(data[5])



file = open("species.csv")
file.readline()
for line in file:
    add_dataset(line.split(','))

pprint.pprint(result)


file.close()
