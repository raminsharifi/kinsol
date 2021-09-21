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
    # Initialize values of the class
    def __init__(self, point_a, point_b, decimal_point=3):
        self.point_a = point_a
        self.point_b = point_b
        self.decimal_point = decimal_point
        self.__var_a = None
        self.__var_b = None
        self.__var_c = None
        self.__error = " "

    def solve(self) -> (str, str):
        """
        This functions calculates the output line of the class.
        :return:
        * output: None, in case of an error. otherwise: String
        * Error: None, when no error is detected, otherwise: String
        """
        can_solve = self.validate_input()
        if can_solve:
            self.__var_a = self.point_a[1] - self.point_b[1]
            self.__var_b = self.point_b[0] - self.point_a[0]
            self.__var_c = self.__var_b * self.point_a[1] + self.__var_a * \
                           self.point_a[0]
        else:
            return None, self.__error
        # check to see the calculations are right.
        can_output = self.after_compute_validation()
        if can_output:
            # If no error is detected, this will run.
            output = self.to_string()
            return output, None
        else:
            # In the case of an error this will run.
            return None, self.__error

    def validate_input(self) -> (bool, str):
        """
        Checks to see if the inputs are of type list.
        They should be numbers with the length of two.
        :return:
        bool.
        True: When no error is detected. otherwise, False.
        """
        try:
            # Checks the inputs to if they are as expected
            assert isinstance(self.point_a, list) and len(
                self.point_a) == 2
            assert isinstance(self.point_b, list) and len(
                self.point_b) == 2
            assert isinstance(self.point_a[0], int) or isinstance(
                self.point_a[0], float)
            assert isinstance(self.point_a[1], int) or isinstance(
                self.point_a[1], float)
            assert isinstance(self.point_b[0], int) or isinstance(
                self.point_b[0], float)
            assert isinstance(self.point_b[1], int) or isinstance(
                self.point_b[1], float)
            assert isinstance(self.decimal_point,
                              int) and self.decimal_point >= 0
        except AssertionError:
            print(
                f"{bcolors.FAIL}*********** Error Detected ***********{bcolors.ENDC}")
            print("Input types Error!")
            self.__error = "Input types Error!"
            return None
        else:
            return True, None

    def after_compute_validation(self) -> (bool):
        """
        after_compute_validation checks to see computed variables are not inf
        or both A and B are zero.
        :return:
        boolean:
        True: When no error is detected. otherwise, False.
        """
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
            self.__error = "Yours inputs for should be less than Infinity!"
            return False
        except ValueError:
            print(
                f"{bcolors.FAIL}******** Error Detected ********{bcolors.ENDC}")
            print("Please input two different points!")
            self.__error = "Please input two different points!"
            return False
        else:
            return True

    def to_string(self) -> str:
        """
        This function will turn the computed variables into the output String.
        :return:
        String

        """
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
