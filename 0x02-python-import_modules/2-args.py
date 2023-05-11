#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count >= 3:
        print("{} arguments:".format(arg_count - 1))
        for i in range(1, arg_count):
            print("{}: {}".format(i, sys.argv[i]))
    elif arg_count == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("0 arguments.")
