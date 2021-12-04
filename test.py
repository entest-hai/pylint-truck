"""
Docstring
"""
MSG = "Hello Hai Tran"

# pylint: disable-msg=C0103
myname = "Hai Tran"


def printMessage(name):
    """
    Docstring
    """
    print(MSG)
    print(name)
    return 1


if __name__ == "__main__":
    printMessage("Hai")
