#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argn = len(sys.argv) - 1
    if argn == 0:
        print("0 arguments.")
    elif argn == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argn))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
