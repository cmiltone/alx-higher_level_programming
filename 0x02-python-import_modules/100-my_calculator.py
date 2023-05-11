#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg_count = len(sys.argv)
    if arg_count == 4:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        ops = ["+", "-", "*", "/"]
        if op in ops:
            #r = 0
            if op == "+":
                r = add(a, b)
            elif op == "-":
                r = sub(a, b)
            elif op == "*":
                r = mul(a, b)
            elif op == "/":
                r = div(a, b)
            print("{} {} {} = {}".format(a, op, b, r))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
