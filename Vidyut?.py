import string
import metaplot

name = "VIDYUT"
import time
nowT = time.ctime()
ver = 1.0
verAge = 0

qna = {
    "hi":"hey",
    "how are you": "I am fine",
    "what is your name" :  name ,
    "how old are you" :  verAge ,
    "what is your version":  ver ,
    "what is the time now ?": nowT,
}

while True:
    qs = input()
    if(qs == "quit"):
        break
    else:
        print(qna[qs])

root = Tk()
root.title("clock")
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('Times new roman',40,'bold') , background = 'purple' , foreground ='white')

lbl.pack(anchor ='center')
time()

mainloop()
