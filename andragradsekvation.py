def create_quad_equa(x1, x2, y):
    if y == 0:
        if x1 == 0:
            equation = f"x(x - {x2}) = y"
        elif x2 == 0:
            equation = f"x(x - {x1}) = y"
        else:
            equation = f"(x - {x1})(x - {x2}) = y"
    else:
        a = y / (x1 * x2)
        b = -a * (x1 + x2)
        c = a * x1 * x1
        equation = f"{a}x^2 + {b}x + {c} = y"

    return equation

def main():
    x1 = float(input("Enter the first Zero Point (X1): "))
    x2 = float(input("Enter the first Zero Point (X2): "))
    y = float(input("Enter the Y-intercept (y): "))
    
    quad_equa = create_quad_equa(x1, x2, y)
    print("The quadratic equation is:", quad_equa)

if __name__ == "__main__":
  main()

confirmation = input("Press ENTER to exit")
