#!/usr/bin/python
#-*- coding: utf-8 -*-

import ftrobopy

__author__= "Stefani, Kuricki Gabriele"
__version__= "Alpha 0.1"
__status__= "In development"
__date__= "10/04/2018"


USB = '192.168.7.2'

txt = ftrobopy.ftrobopy('auto') #Connessione al controoler

Assex = txt.motor(1)
Assey = txt.motor(2)
Assez = txt.motor(3)

compr = txt.output(7)

tastoresetx = txt.input(1)
tastoresety = txt.input(2)
tastoresetz = txt.input(3)


def Reset():
    Assey.setSpeed(512)
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

Reset()
