import math


def point_to_line(point_a: list, point_b: list, decimal_point=3) -> str:
    try:
        assert isinstance(point_a, list) and len(point_a) == 2
        assert isinstance(point_b, list) and len(point_b) == 2
    except AssertionError:
        print("Could Not verify your inputs are of type list, or length two")
        return "No Answer, Error raised"
    try:
        var_a = point_a[1] - point_b[1]
        var_b = point_b[0] - point_a[0]
        var_c = var_b * point_a[1] + var_a * point_a[0]
        assert math.isinf(var_a) is not True and math.isinf(var_b) is not True
        if var_a == 0 and var_b == 0:
            raise ValueError(
                "Both points were equal, Please provide two different points"
            )

    except TypeError as err:
        print("Make sure your inputs are numerical!")
        print(f"Your error is: {err}.")
        return "No Answer, Error raised"
    except AssertionError as err:
        print("Yours inputs for should be less than Infinity!")
        print(f"Your error is: {err}!")
        return "No Answer, Error raised"
    except ValueError as err:
        print("Please input two different points!")
        print(f"Your error is: {err}!")
        return "No Answer, Error raised"

    else:
        if var_a == 0:
            outline = f"{var_b:.{decimal_point}f} * Y " \
                      f"= {var_c:.{decimal_point}f} with A = 0"
        elif var_b == 0:
            outline = f"({var_a:.{decimal_point}f}) * X " \
                      f"= {var_c:.{decimal_point}f} with B = 0"
        else:
            outline = f"({var_a:.{decimal_point}f}) * X " \
                      f"+ ({var_b:.{decimal_point}f}) * Y " \
                      f"= {var_c:.{decimal_point}f}"

        return outline
