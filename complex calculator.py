from sys import stdin
import math

def readln():
    return stdin.readline().strip()

def sum_comps(num1,num2):
    res = []
    res.append(num1[0] + num2[0])
    res.append(num1[1] + num2[1])
    return res

def res_comp(num1,num2):
    res = []
    res.append(num1[0] - num2[0])
    res.append(num1[1] - num2[1])
    return res

def mult_comp(num1,num2):
    res = []
    res.append((num1[0]*num2[0])-(num1[1]*num2[1]))
    res.append((num1[0]*num2[1])+(num2[0]*num1[1]))
    return res

def div_comp(num1,num2):
    res = []
    a = num1[0]
    b = num1[1]
    c = num2[0]
    d = num2[1]
    res.append(((a*c) + (b*d))/((c^2)+(d^2)))
    res.append(((b*c) - (a*d))/((c^2)+(d^2)))
    return res

def mod_comp(num1):
    a = num1[0]
    b = num1[1]
    return math.sqrt((a^2)+(b^2))

def conj_comp(num1):
    return mult_comp(num1,[-1,0])

"""""def main():
    sel = None
    while sel != 0:
        print("calculadora de numeros complejos")
        print("1) suma")
        print("2) resta")
        print("3) multiplicacion")
        print("4) division")
        print("5) modulo")
        print("6) conjugado")
        print("7) conversiones")
        print("8) retornar la fase de un numero complejo")
        print("0) salir")
        sel = int(readln())
        if sel == 1:
            print("escriba la parte real del numero")
        elif sel == 2:
        elif sel == 3:
        elif sel == 4:
        elif sel == 5:
        elif sel == 6:
        elif sel == 7:
        elif sel == 8:
        elif sel == 0:
            return 0
        else:
            print("ingrese un numero valido")


main()"""""