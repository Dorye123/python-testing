import json
import re

# work with json object 
jsonobjectAsString = '{"value1": "1", "value2": "2", "value3": "3"}'



# change _R and _RE to _X
dictobject = { "value4":"2728_RE", "value1":"1_R", "value2":2, "value3":"3_RE" }
dictobject["value3"] = 4
print(len(dictobject))
for i in dictobject:
    if type(dictobject[i]) == str:
        reoutput = re.match("\w+_[R|RE]$",dictobject[i])  
        if reoutput:
            splitedObject = re.split("_", dictobject[i])
            print(splitedObject[0:-1])
            # dictobject[i] = splitedObject[0..-1] + "_X"
    else: 
        pass
    


# print(dictobject["value3"])
# with open("value.json", "w") as j:
#     json.dump(jsonstring, j)

# dir(jsonstring)
# print(jsonstring)