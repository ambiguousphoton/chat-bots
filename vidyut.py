name = "VIDYUT chat bot"
import time
nowT = time.ctime()
ver = 1.0
verAge = 0
creator = "Krishna"

qna = {
    "hi":"hey",
    "how are you": "I am fine",
    "what is your name" :  name ,
    "how old are you" :  verAge ,
    "what is your version":  ver ,
    "what is the time now ?": nowT,
    "Who is your creator ?": Vyoam,
    "Who is your cretors creator ?": creator,
}

while True:
    qs = input()
    if(qs == "quit"):
        break
    else:
        print(qna[qs])
