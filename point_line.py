"""Point to Line function

This script allows the user to input two different points in Cartesian
coordinates and output the line which includes the input points
in the form of: Ax + By = C

    Functions in this file:
    -----------------------
    * validate_input
    * after_compute_validation
    * to_string
    * solve
"""
import math
import bcolors


class PointToLine:
    @classmethod
    def __init__(self, point_a, point_b, decimal_point=3):
        self.point_a = point_a
        self.point_b = point_b
        self.decimal_point = decimal_point

    @classmethod
    def validate_input(self) -> (bool, str):
        try:
            # Checks the inputs to if they are as expected
            assert isinstance(self.point_a, list) and len(self.point_a) == 2
            assert isinstance(self.point_b, list) and len(self.point_b) == 2
            assert isinstance(self.decimal_point,
                              int) and self.decimal_point >= 0
        except AssertionError:
            print(
                f"{bcolors.FAIL}*********** Error Detected ***********{bcolors.ENDC}")
            print("Input types Error!")
            return None, "Input types Error!"
        else:
            return True, None

    @staticmethod
    def after_compute_validation(var_a, var_b) -> (bool, str):
        try:
            assert math.isinf(var_a) is not True and math.isinf(
                var_b) is not True
            if var_a == 0 and var_b == 0:
                raise ValueError
        except AssertionError as err:
            print(
                f"{bcolors.FAIL}******** Error Detected ********{bcolors.ENDC}")
            print("Yours inputs for should be less than Infinity!")
            print(f"Your error is: {err}!")
            return None, "Yours inputs for should be less than Infinity!"
        except ValueError:
            print(
                f"{bcolors.FAIL}******** Error Detected ********{bcolors.ENDC}")
            print("Please input two different points!")
            return None, "Please input two different points!"
        else:
            return True, None

    @classmethod
    def to_string(self, var_a, var_b, var_c) -> str:
        if var_a == 0:
            output = (
                f"{var_b:.{self.decimal_point}f} * Y "
                f"= {var_c:.{self.decimal_point}f} with A = 0"
            )
        elif var_b == 0:
            output = (
                f"({var_a:.{self.decimal_point}f}) * X "
                f"= {var_c:.{self.decimal_point}f} with B = 0"
            )
        else:
            output = (
                f"({var_a:.{self.decimal_point}f}) * X "
                f"+ ({var_b:.{self.decimal_point}f}) * Y "
                f"= {var_c:.{self.decimal_point}f}"
            )
        return output

    @classmethod
    def solve(self) -> (str, str):
        can_solve, error = self.validate_input()
        if can_solve and error is None:
            var_a = self.point_a[1] - self.point_b[1]
            var_b = self.point_b[0] - self.point_a[0]
            var_c = var_b * self.point_a[1] + var_a * self.point_a[0]
        else:
            return None, error
        can_output, error = self.after_compute_validation(var_a, var_b)
        if can_output and error is None:
            output = self.to_string(var_a, var_b, var_c)
            return output, None
        else:
            return None, error
