# functions that recalled in the other python files
import  random

feetinmile = 5280
metersinkilometer  = 1000
beateles = ["john lennon","paul mcCartney","george harrison","ringo star"]

def ger_file_ext(filename):
    return  filename[filename.index(".") + 1:]

def roll_dice(num):
    return  random.randint(1,num)
