srk={
    "srk2" :{
    "institution_name" : "SRK Institution",
    "address": "firozabad",
    "code" : .0007,
    "srk_cse": {
        "director_name": "DR. U.S Gupta",
        "course" : ["BCA","BBA","B.ED"],
        "BCA":{
            "HOD": "Sonali Sharma",
           "fees": 90000
        },
        "BBA": {
            "HOD": "charu Lahri",
            "fees": 70000
        },
        "B.ED": {
            "HOD": "Sumitra Devi",
            "fees": 100000
        }
    }}
}
print(len(srk.keys()) )
print(srk.keys())# only  outer key returns , sub dictionary 's inner keys not return.in a form of tuple.
print(srk.values()) # this method use to return all values in dictionary also return sub dictionary's values.in a form of tuple
print(srk.items()) #  this method is use to return all keys and values also sub dictionary.
print(srk.get("srk2")) # retuen the key.
new={"city": "up","address": "firozabad"}
srk.update(new)
print(srk)