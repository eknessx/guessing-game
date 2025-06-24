#write a python programm to concatinate the following dictionaries to create a new one.


dict1={
    "user":"majd",
    "id":"client",
}

dict2={
    "lvl":21,
    "status":"active",
}
dict3={}
dict3=dict1|dict2
print(dict3)
