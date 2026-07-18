import sys


try:
    with open(sys.argv[1], "w") as f:
        _ = f.write("direct\n")
except OSError:
    pass
