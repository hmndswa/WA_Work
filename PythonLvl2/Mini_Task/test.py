x = "global"


def outer():
    # x = "enclosing"
    def inner():
        print("inner sees:", x)

    inner()
    print("outer sees:", x)


outer()
print("global sees:", x)
