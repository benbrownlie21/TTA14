x = input("Please enter a number: ")


def one_param(x):
    double = int(x + x)
    triple = int(x + x + x)
    quad = int(x + x + x + x)
    result = int(x) + double + triple + quad
    print(f"{x} + {x}{x} + {x}{x}{x} + {x}{x}{x}{x} = {result}")


one_param(x)
