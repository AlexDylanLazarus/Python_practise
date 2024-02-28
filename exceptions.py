def math_divide(n1, n2):

    try:
        result = n1 / n2
        print("the answer is", result)

    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        # when no errors happen
        print("Division was successsful")
    finally:
        # No Error. We generally run cleanup code here.
        print("Operation done")


math_divide(10, 5)

print("hiii")
