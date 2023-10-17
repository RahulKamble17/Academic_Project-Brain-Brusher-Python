import time
from plyer import notification
import random
from PyDictionary import PyDictionary
dictionary = PyDictionary()

file= open("dict.txt")
words= file.read().split("\n")
def get_word():
    valid_word = False
    while(not valid_word):
        index=random.randint(0,len(words)-1)#235886
        word= words[index]
        if(word[0].islower() and len(word)>2):
            valid_word=True
            return word
def define_word():
    valid_word = False
    while(not valid_word):
        word=get_word()
        if(dictionary.meaning(word, disable_errors=True)):
            #return()
            defs= dictionary.meaning(word)
            for key,value in defs.items():
                return(word.upper()+"\n"+str(key)+": "+str(value).strip("[]\'\"").replace("\'",""))
            valid_word=True
def_line=define_word()

test=get_word()

def notii():
    notification.notify(
        title="Word of the day!",
        message=def_line,
        timeout=60
    )

notii()

while True:
    notification.notify(
        title="Did you drink water today?",
        message="About 3.7 liters of fluids for men & 2.7 liters for women is required daily",
        app_icon="C:\\Users\\Admin\\Desktop\\project\\Scheduler\\Rade8-Drinx-X-water.ico",
        timeout=15
    )
    time.sleep(60*60)

    notification.notify(
		title="test",
		message="testing"
	)