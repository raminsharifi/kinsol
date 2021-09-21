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

    def __init__(self, point_a, point_b, decimal_point=3):
        self.point_a = point_a
        self.point_b = point_b
        self.decimal_point = decimal_point
        self.__var_a = 0
        self.__var_b = 0
        self.__var_c = 0

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

    def after_compute_validation(self) -> (bool, str):
        try:
            assert math.isinf(self.__var_a) is not True and math.isinf(
                self.__var_b) is not True
            if self.__var_a == 0 and self.__var_b == 0:
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

    def to_string(self) -> str:
        if self.__var_a == 0:
            output = (
                f"{self.__var_b:.{self.decimal_point}f} * Y "
                f"= {self.__var_c:.{self.decimal_point}f} with A = 0"
            )
        elif self.__var_b == 0:
            output = (
                f"({self.__var_a:.{self.decimal_point}f}) * X "
                f"= {self.__var_c:.{self.decimal_point}f} with B = 0"
            )
        else:
            output = (
                f"({self.__var_a:.{self.decimal_point}f}) * X "
                f"+ ({self.__var_b:.{self.decimal_point}f}) * Y "
                f"= {self.__var_c:.{self.decimal_point}f}"
            )
        return output

    def solve(self) -> (str, str):
        can_solve, error = self.validate_input()
        if can_solve and error is None:
            self.__var_a = self.point_a[1] - self.point_b[1]
            self.__var_b = self.point_b[0] - self.point_a[0]
            self.__var_c = self.__var_b * self.point_a[1] + self.__var_a * \
                           self.point_a[0]
        else:
            return None, error
        can_output, error = self.after_compute_validation()
        if can_output and error is None:
            output = self.to_string()
            return output, None
        else:
            return None, error
