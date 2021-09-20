import argparse
import os
import bcolors
from point_to_line import point_to_line

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "-a",
    "--point_a",
    nargs=2,
    type=float,
    help="Should be numerical two values of type int / float. Seperated by space.",
)
parser.add_argument(
    "-b",
    "--point_b",
    nargs=2,
    type=float,
    help="Should be numerical two values of type int / float. Seperated by space",
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
    "-s",
    "--save_to_file",
    default=True,
    type=bool,
    help="accpets: Boolean, if True: " "Will write to csv file",
)
args = parser.parse_args()

if __name__ == "__main__":
    point_a = args.point_a
    point_b = args.point_b
    decimal_point = args.decimal_points

    output, Error = point_to_line(point_a, point_b, decimal_point)

    if output is not None:
        print(f"{bcolors.BOLD}*********** OUTPUT ***********{bcolors.ENDC}")
        print(f"{bcolors.BITALIC}{output}{bcolors.ENDC}")

    if args.save_to_file:
        print("*********** Saving output to CSV file ***********")
        if os.path.isfile("point_to_file.csv"):
            with open("point_to_file.csv", "a", encoding="utf-8") as f:
                f.write(
                    f"\n{point_a[0]},{point_a[1]},{point_b[0]}, {point_b[1]}, "
                    f"{decimal_point}, {output}, {Error}"
                )
        else:
            with open("point_to_file.csv", "w", encoding="utf-8") as f:
                f.write("X1, Y1, X2, Y2, decimal_point, line_output, Error\n")
                f.write(
                    f"{point_a[0]},{point_a[1]},{point_b[0]}, {point_b[1]}, "
                    f"{decimal_point}, {output}, {Error}"
                )
        print(" Results saved to 'point_to_file.csv'")

    print(f"{bcolors.OKMSG}*********** Done! ***********{bcolors.ENDC}")
