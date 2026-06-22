import math

def Converter(ângulo):
    rad = (3.14159265*ângulo)/180
    return rad

def Calculardh(rad,distância):
    dh =  math.cos(rad)*distância
    return dh

def Calculardt(rad, distância):
    dt = distância/math.cos(rad)
    return dt

def Calcularh1(rad, distância):
    h = math.sin(rad)*distância
    return h

def Calcularh2(rad, distância):
    h = math.tan(rad)*distância
    return h