import ftrobopy
import time
import numpy

#Inutile
__author__= "Stefani, Kuricki Gabriele"
__version__= "Alpha 0.1"
__status__= "In development"
__date__= "10/04/2018"

#Connessione al controller
USB = '192.168.7.2'
txt = ftrobopy.ftrobopy('auto')

#Dichiarazione Motori
Assex = txt.motor(1)
Assey = txt.motor(2)
Assez = txt.motor(3)

#Dichiarazione compressore
compr = txt.output(7)

#Dichiarazione tasti
tastoresetx = txt.input(1)
tastoresety = txt.input(2)
tastoresetz = txt.input(3)

#Posizioni
uno = {
    "1" : [3150,1350]}
due = {
    "1" : [3500,1700],
    "2" : [3890,2075]}
tre = {
    "1" : [2125,1350],
    "2" : [3890,1325],
    "3" : [1425,2075]}
quattro = {
    "1" : [2125,350],
    "2" : [2125,380],
    "3" : [1425,380],
    "4" : [1425,350]}
cinque = {
    "1" : [3150,350],
    "2" : [3890,350],
    "3" : [3890,380],
    "4" : [3150,380],
    "5" : [3500,0]}
centro = {
    "1" : [2650,850]}

#Funzioni varie
def Reset():
    Assey.setSpeed(450)
    Assez.setSpeed(512)
    Assex.setSpeed(512)
    while (tastoresetx.state() == 0 or tastoresety.state() == 0 or tastoresetz.state() == 0):
        if (tastoresety.state() == 1):
            Assey.stop()
        if (tastoresetx.state() == 1):
            Assex.stop()
        if (tastoresetz.state() == 1):
            Assez.stop()
    print("Fatto")

def PresaPalline():
    Assey.setDistance(500)
    Assez.setDistance(250)
    Assex.setDistance(350)
    Assex.setSpeed(-512)
    Assez.setSpeed(-512)
    Assey.setSpeed(-512)
    txt.updateWait(3)
    Assez.setDistance(350)
    Assez.setSpeed(512)
    txt.updateWait(1)
    compr.setLevel(512)
    txt.updateWait(0.5)
    Assez.setDistance(400)
    Assez.setSpeed(-512)

def ReleasePalline():
    while not Assex.finished():
        txt.updateWait()
    Assez.setDistance(225)
    Assez.setSpeed(512)
    txt.updateWait(1)
    compr.setLevel(0)

def GoTo(**coord):
    a=coord.get("1")
    if(a[1] == 380):
        Assey.setDistance(a[1])
        Assey.setSpeed(512)
        Assex.setDistance(a[0])
        Assex.setSpeed(-512)
    else:
        Assex.setDistance(a[0])
        Assey.setDistance(a[1])
        Assex.setSpeed(-512)
        Assey.setSpeed(-512)

def RimozionePalline():
    GoTo()
    Assez.setDistance(100)
    Assez.setSpeed(512)
    txt.updateWait(3)
    compr.setLevel(512)

#Inizio programma

Reset()
print("Resettato")

txt.updateWait(1)
PresaPalline()
print("Pallina Presa")

#Casino
print("Il dato e'%d") % (dado)

if(dado == 1):
    GoTo(**uno)

elif(dado == 2):
    GoTo(**due)

elif(dado == 3):
    GoTo(**tre)

elif(dado == 4):
    GoTo(**quattro)

elif(dado == 5):
    GoTo(**cinque)
print("Go To fatto")

txt.updateWait(1)
ReleasePalline()

txt.updateWait(1)
Reset()
