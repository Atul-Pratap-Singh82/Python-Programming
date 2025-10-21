srk={
    "institution_name" : "SRK Institution",
    "address": "firozabad",
    "code" : .0007,
    "srk_cse": {
        "director_name": "DR. U.S Gupta",
        "course" : ["BCA","BBA","B.ED"],
        "BCA":{
            "HOD": "Sonali Sharma",
           "fees": "90000"
        },
        "BBA": {
            "HOD": "Charu Lahri",
            "fees": "70000"
        },
        "B.ED": {
            "HOD": "Sumitra Devi",
            "fees": "100000"
        }
    }
}
srk["srk_cse"]["BBA"]["HOD"] = "Shivam Bhrti"
print(srk)