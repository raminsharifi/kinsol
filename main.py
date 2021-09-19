import argparse
from pointToLine import point_to_line
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-a', '--point_a', nargs='+', type=float,
                    help='Should be numerical values of type int / float.')
parser.add_argument('-b', '--point_b', nargs='+', type=float,
                    help='Should be numerical values of type int / float.')
parser.add_argument('-d', '--decimal_points', default=3, type=int,
                    help='Specifies the number of decimal points in output. '
                         'default value is 3.')
parser.add_argument('-s', '--save_to_file', default=False, type=bool,
                    help='Should be numerical values of type int / float.')
args = parser.parse_args()

if __name__ == '__main__':
    point_a = args.point_a
    point_b = args.point_b
    decimal_point = args.decimal_points

    output = point_to_line(point_a, point_b, decimal_point)
    if args.save_to_file:
        if os.path.isfile('point_to_file.csv'):
            with open('point_to_file.csv', 'a+') as f:
                f.write(f"\n{point_a}, {point_b}, {decimal_point}, {output}")
        else:
            with open('point_to_file.csv', 'a') as f:
                f.write("point_a, point_b, decimal_point, line_output\n")
                f.write(f"{point_a}, {point_b}, {decimal_point}, {output}")

