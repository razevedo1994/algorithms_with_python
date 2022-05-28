"""Funcoes logaritmicas sao a forma de descobrir
a potencia que voce deve elevar uma base para
chegar a outro numero."""

from itertools import count
import math

"""
log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.
"""
x = int(input("Digite um numero o qual voce deseja descobrir o logaritmo: "))
base = int(input("Digite a base na qual sera calculada a funcao: "))

print(f"O logaritmo de {x} na base {base} eh: {math.log(x, base)}")


def calc_log(x: int, base: int):
    count = 0
