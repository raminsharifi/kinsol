"""Point to Line function

This script allows the user to input two different points in Cartesian
coordinates and output the line which includes the input points
in the form of: Ax + By = C

    Functions in this file:
    -----------------------
    * point_to_line
"""

import math
import bcolors


def point_to_line(point_a: list, point_b: list, decimal_point=3) -> (str, str):
    """Gets two points and outputs the line in the format: Ax+By = C

    Parameters
    ----------
    point_a : list
        [x,y] is the expected input to the function for the first point.
    point_b : list
        [x,y] is expected input to the function for the second point.
    decimal_point: int
        This gives you the freedom to output with the number of decimal points desired.



    Returns
    -------
    String, String
        First output is the output. If error detected, returns None.
        Second output is the error, if detected. else, returns None.
    """
    try:
        # Checks the inputs to if they are as expected
        assert isinstance(point_a, list) and len(point_a) == 2
        assert isinstance(point_b, list) and len(point_b) == 2
        assert isinstance(decimal_point, int) and decimal_point >= 0
    except AssertionError:
        print(f"{bcolors.FAIL}*********** Error Detected ***********{bcolors.ENDC}")
        print("Input types Error!")
        return None, "Input types Error!"
    try:
        # Computing A, B, C according to the input.
        var_a = point_a[1] - point_b[1]
        var_b = point_b[0] - point_a[0]
        var_c = var_b * point_a[1] + var_a * point_a[0]
        assert math.isinf(var_a) is not True and math.isinf(var_b) is not True
        if var_a == 0 and var_b == 0:
            raise ValueError
        # Handling different Error Scenarios and return None as output.
    except TypeError as err:
        print(f"{bcolors.FAIL}******** Error Detected ********{bcolors.ENDC}")
        print("Make sure your inputs are numerical!")
        print(f"Your error is: {err}.")
        return None, "Make sure your inputs are numerical!"
    except AssertionError as err:
        print(f"{bcolors.FAIL}******** Error Detected ********{bcolors.ENDC}")
        print("Yours inputs for should be less than Infinity!")
        print(f"Your error is: {err}!")
        return None, "Yours inputs for should be less than Infinity!"
    except ValueError as err:
        print(f"{bcolors.FAIL}******** Error Detected ********{bcolors.ENDC}")
        print("Please input two different points!")
        return None, "Please input two different points!"

    else:
        # output different strings based on different A, B.
        # Error would be returned as None
        if var_a == 0:
            output = (
                f"{var_b:.{decimal_point}f} * Y "
                f"= {var_c:.{decimal_point}f} with A = 0"
            )
        elif var_b == 0:
            output = (
                f"({var_a:.{decimal_point}f}) * X "
                f"= {var_c:.{decimal_point}f} with B = 0"
            )
        else:
            output = (
                f"({var_a:.{decimal_point}f}) * X "
                f"+ ({var_b:.{decimal_point}f}) * Y "
                f"= {var_c:.{decimal_point}f}"
            )

        return output, None
