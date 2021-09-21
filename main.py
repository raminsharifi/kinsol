# -*- coding: utf-8 -*-
"""Runner for point_to_line function

This is the runner file.
    Parameters
    ----------
    -a, --point_a: list, inputs seperated by space. like: -a 2 5 --> a = [2, 5]
    -b, --point_b: list, inputs seperated by space. like: -b 2 5 --> b = [2, 5]
    -d, --decimal_points: int. The default for this is 3.
    --save_to_csv, flag, which runs by default.
    --no_save, flag, for not saving the output to a CSV file.


    usage example
    --------------
    python main.py -a 1 1 -b 1.2 3.4 -d 5 --save_to_csv

"""

import argparse
import os
import bcolors
from point_line import PointToLine


def arguments():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "-a",
        "--point_a",
        nargs=2,
        type=float,
        help="Should be two values of type int/float. Seperated by space.",
    )
    parser.add_argument(
        "-b",
        "--point_b",
        nargs=2,
        type=float,
        help="Should be two values of type int/float. Seperated by space.",
    )
    parser.add_argument(
        "-d",
        "--decimal_points",
        default=3,
        type=int,
        help="Specifies the number of decimal points in output. "
             "Should be greater or equal to zero."
             "default value is 3.",
    )
    parser.add_argument(
        "--save_to_csv",
        dest="save",
        action="store_true",
        help="If used, will save the results into a CSV file.True by default.",
    )
    parser.add_argument(
        "--no_save",
        dest="save",
        action="store_false",
        help="Will not save the results to CSV. False by default.",
    )
    parser.set_defaults(save=True)
    return parser.parse_args()


def save(saveFlag: bool):
    # Checks to see if the output/error needs to be saved.
    if saveFlag:
        print("*********** Saving output to CSV file ***********")

        # Checks to see if there is a file existing and writes to it.
        if os.path.isfile("point_to_file.csv"):
            with open("point_to_file.csv", "a", encoding="utf-8") as f:
                f.write(
                    f"\n{point_a[0]},{point_a[1]},{point_b[0]}, {point_b[1]}, "
                    f"{decimal_point}, {output}, {Error}"
                )
        else:
            # Runs when there is no existing file existing.
            with open("point_to_file.csv", "w", encoding="utf-8") as f:
                f.write("X1, Y1, X2, Y2, decimal_point, line_output, Error\n")
                f.write(
                    f"{point_a[0]},{point_a[1]},{point_b[0]}, {point_b[1]}, "
                    f"{decimal_point}, {output}, {Error}"
                )
        print(" Results saved to 'point_to_file.csv'")

    print(f"{bcolors.OKMSG}*********** Done! ***********{bcolors.ENDC}")


def print_to_terminal(output):
    if output is not None:
        # runs when there is no error detected.
        print(f"{bcolors.BOLD}*********** OUTPUT ***********{bcolors.ENDC}")
        print(f"{bcolors.BITALIC}{output}{bcolors.ENDC}")


if __name__ == "__main__":
    # Saving the input to local variables.
    args = arguments()
    point_a = args.point_a
    point_b = args.point_b
    decimal_point = args.decimal_points
    save_to_file = args.save

    # Runs the function.
    my_point_to_line = PointToLine(point_a, point_b, decimal_point)
    output, Error = my_point_to_line.solve()

    # runs when there is no error detected.
    print_to_terminal(output)

    save(args.save)
