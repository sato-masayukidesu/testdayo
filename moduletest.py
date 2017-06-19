
import os

CurrentDir = os.getcwd()


def test1(inp):
    """change dir to input()"""
    try:
        if os.getcwd() == CurrentDir:
            os.mkdir(inp)
            print("make dir")
    except FileExistsError:
        pass
    if os.getcwd() == CurrentDir:
        os.chdir(inp)


def test2(inp):
    try:
        os.mkdir(inp)
        print("make dir 2")
    except FileExistsError:
        pass
