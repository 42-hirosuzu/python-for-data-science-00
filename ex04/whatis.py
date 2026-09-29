import sys


args = sys.argv[1:]
if len(args) > 1:
    print("AssertionError: more than one argument is provided")
elif len(args) == 1:
    try:
        n = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
