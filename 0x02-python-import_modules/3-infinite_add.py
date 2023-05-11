#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _sum = 0
    count = len(sys.argv)
    for i in range(1, count):
        _sum += int(sys.argv[i])
    print("{}".format(_sum))
