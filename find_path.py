
import sys
import os
import os.path as path


if __name__ == "__main__":
    print(path.dirname(__file__))
    print(path.abspath(__file__))
    print(path.dirname(path.curdir))
    print(path.realpath(path.curdir))
    print(path.dirname(path.abspath(__file__)))