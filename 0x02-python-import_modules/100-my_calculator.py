#!/usr/bin/python3
if name == "main":
    import calculator_1
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    if op == "+":
        print(
            "{} + {} = {}".format(
                sys.argv[1],
                sys.argv[3],
                calculator_1.add(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    elif op == "-":
        print(
            "{} - {} = {}".format(
                sys.argv[1],
                sys.argv[3],
                calculator_1.sub(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    elif op == "*":
        print(
            "{} * {} = {}".format(
                sys.argv[1],
                sys.argv[3],
                calculator_1.mul(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    elif op == "/":
        print(
            "{} / {} = {}".format(
                sys.argv[1],
                sys.argv[3],
                calculator_1.div(int(sys.argv[1]), int(sys.argv[3])),
            )
        )
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
