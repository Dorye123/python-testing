import json
import re

# work with json object 
jsonobjectAsString = { "value4":"2728_RE", "value1":"1_R", "value2":2, "value3":"3_RE" }
with open("data_file.json", "w") as write_file:
    json.dump(jsonobjectAsString, write_file)

jsonString = json.dumps(jsonobjectAsString)
print(jsonString)
# print(json.loads("data_file.json"))

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
data_decode = json.dumps(data)
print(json_string)
print(data)
print(data_decode)
print(type(data))
print(type(data_decode))


# # change _R and _RE to _X
dictobject = { "value4":"2728_RE", "value1":"1_R", "value2":2, "value3":"3_RE" }
# dictobject["value3"] = 4
print(len(dictobject))
for i in dictobject:
    if type(dictobject[i]) == str:
        reoutput = re.match("\S+_+RE?$",dictobject[i])  
        if reoutput:
            print(i)
            splitedObject = re.split("_", dictobject[i])
            print(splitedObject)
            dictobject[i] = splitedObject[0] + "_X"
            print(dictobject[i])
    else: 
        pass

print(dictobject)
    

