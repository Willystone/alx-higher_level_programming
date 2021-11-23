#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

argc = len(argv)

if _name_ == "_main_":

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opertors = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(operators.keys()):
        print(Unkown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print(f"{a} {argv[2]} {b} = {operators[agrv[2]](a, b)}")
    
