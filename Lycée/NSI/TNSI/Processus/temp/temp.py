from time import sleep
import psutil
n=int(input("période"))
while True:
    tempsinfos=psutil.sensors_temperatures()
    # print(tempsinfos)
    t=tempsinfos["coretemp"][0].current
    print("température du coeur 0 :", t)
    sleep(n)