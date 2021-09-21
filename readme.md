## Point to line Python Program

This python program will get two distinct input and outputs the line which
passes through these points. The points should be in *Cartesian* coordinates.

## How to run this code:

1. Please clone this repo using:
   `git clone git@github.com:raminsharifi/kinsol.git`.
2. Install the required packages using: `pip install -r requirements.txt`
3. You are all set. Keep in mind that this runs on Python 3.6+.
4. You can try the code using the following flags:

```
python main.py -a 1 1 -b 2 2 -d 3 --save_to_csv
```

OR

```
python main.py --point_a 1 1 --point_b 2 2 --decimal_point 3 --no_save
```

## pytest

The `PointToLine` class has been unit tested with pytest in different
scenarios. The Unit tests are also, included in this repository in the file
named: `test_point_to_line.py`.

## Save To CSV function

If you decide to save your results in a csv file, you can add `--save_to_csv`,
when you are running your calculations using `main.py`.
> Please note that the results are saved by default.

If you don't want to save your results, you can use `--no_save` when running
`main.py`.
