def create_quadratic_equation(x1, x2, y):
    if y == 0:
        # If y-intercept is 0, it means one of the roots is also 0
        # In this case, we can factor out x from one of the roots to get the quadratic equation
        if x1 == 0:
            equation = f"x(x - {x2}) = 0"
        elif x2 == 0:
            equation = f"x(x - {x1}) = 0"
        else:
            equation = f"(x - {x1})(x - {x2}) = 0"
    else:
        a = y / (x1 * x2)
        b = -a * (x1 + x2)
        c = a * x1 * x2
        equation = f"{a}x^2 + {b}x + {c} = 0"

    return equation

def main():
    x1 = float(input("Enter the first zero point (x1): "))
    x2 = float(input("Enter the second zero point (x2): "))
    y = float(input("Enter the y-intercept: "))

    quadratic_equation = create_quadratic_equation(x1, x2, y)
    print("The quadratic equation is:", quadratic_equation)

if __name__ == "__main__":
    main()

confirmation = input("Press ENTER to exit")