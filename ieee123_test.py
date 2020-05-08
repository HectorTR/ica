import os
import gridlabd


def find(criteria):
    finder = criteria.split("=")
    if len(finder) < 2:
        raise Exception("find(criteria='key=value'): criteria syntax error")
    objects = gridlabd.get("objects")
    result = []
    for name in objects:
        item = gridlabd.get_object(name)
        if finder[0] in item and item[finder[0]] == finder[1]:
            if "name" in item.keys():
                result.append(item["name"])
            else:
                result.append("%s:%s" % (item["class"], item["id"]))
    return result


def on_init(t):
    #houses = find("class=house")
    #global recorder
    #recorder = open("house.csv", "w")
    #recorder.write("name,datetime,temperature\n")
    objects = gridlabd.get("objects")
    print(type(objects))
    print(objects)
    return True


def record_house(name, t):
    global recorder
    if recorder:
        house = gridlabd.get_object(name)
        recorder.write("%s,%s,%s\n" % (house["name"], house["clock"], house["air_temperature"]))
    return True


def on_term(t):
    recorder.close()

print ("Succesful Run")

