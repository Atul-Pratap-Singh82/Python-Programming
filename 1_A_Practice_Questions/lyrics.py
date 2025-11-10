import time

import sys
def dprint():
    ly=[
        "Pal-pal jeena muhaal mera tere bina",
        "Yeh saare nashe bekaar teri aankhon ke siva",
        "Ghar nahi jaata, main bahar, rehta tera intezaar",
        "Mere khwabon mein aa na karke 16 singhaar.", 
        "Main ab kyun hosh mein aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun todun khud se jo the waade?",
        "Ke ab yeh ishq nibhana nahi",
        "Mein morrun tum se jo ye chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaanay mera dard ",
        "Tujhe yeh nazar kyun aata nahi?"
    ]
    delays=[
        0.3,0.3,0.4,0.3,0.3,0.3,0.8
    ]
    print("Pal Pal :\n")
    time.sleep(1.2)

    for i,line in enumerate(ly):
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i<len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

dprint()
