#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:\n{}: {:s}".format(argc, argc, sys.argv[1]))
    else:
        list_count = 1
        print("{} arguments:".format(argc))
        while list_count <= argc:
            print("{}: {:s}".format(list_count, sys.argv[list_count]))
            list_count += 1
