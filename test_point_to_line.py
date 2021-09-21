import math
import pytest
from point_line import PointToLine


@pytest.mark.regular
def test_PointToLine_int():
    assert PointToLine([1, 1], [2, 2]).solve() == (
        "(-1.000) * X + (1.000) * Y = 0.000", None)
    assert PointToLine([1, 2], [2, 2]).solve() == (
        "1.000 * Y = 2.000 with A = 0", None)
    assert PointToLine([0, 0], [2, -7]).solve() == (
        "(7.000) * X + (2.000) * Y = 0.000", None)


#
@pytest.mark.regular
def test_PointToLine_float():
    assert PointToLine(
        [1.367123, 1.7263487], [2.276492, 6.737453], decimal_point=10
    ).solve() == (
               "(-5.0111043000) * X + (0.9093690000) * Y = -5.2809079530",
               None)
    assert PointToLine([1.23, 2], [2.78, 2]).solve() == (
        "1.550 * Y = 3.100 with A = 0", None)
    assert PointToLine([1234.232, 1000], [10, 2], decimal_point=3).solve() == (
        "(998.000) * X + (-1224.232) * Y = 7531.536",
        None,
    )


#
#
@pytest.mark.error
def test_PointToLine_same():
    assert PointToLine([1, 1], [1, 1]).solve() == (
        None, "Please input two different points!")
    assert PointToLine([0, 0], [0, 0]).solve() == (
        None, "Please input two different points!")
    assert PointToLine([1000, 1000], [1000, 1000]).solve() == (
        None,
        "Please input two different points!",
    )


@pytest.mark.error
def test_PointToLine_inf():
    assert PointToLine([math.inf, 1000], [1000, 1000]).solve() == (
        None,
        "Yours inputs for should be less than Infinity!",
    )
    assert PointToLine([-6427384, 1000], [1000, math.inf]).solve() == (
        None,
        "Yours inputs for should be less than Infinity!",
    )
    assert PointToLine([-6427328973428937423484, 1000],
                       [1000, math.inf]).solve() == (
               None,
               "Yours inputs for should be less than Infinity!",
           )


@pytest.mark.error
def test_PointToLine_input_type():
    assert PointToLine(["asd", 1000], [10, 20.234]).solve() == (
        None,
        "Input types Error!",
    )
    assert PointToLine([1234.232, 1000], [10, "dsfaw"]).solve() == (
        None,
        "Input types Error!",
    )
    assert PointToLine([1234.232, 1000], [10, " "]).solve() == (
        None,
        "Input types Error!",
    )


@pytest.mark.error
def test_PointToLine_decimal():
    assert PointToLine([1234.232, 1000], [10, 2],
                       decimal_point=1.3).solve() == (
               None,
               "Input types Error!",
           )
    assert PointToLine([1234.232, 1000], [10, 2],
                       decimal_point=-1.3).solve() == (
               None,
               "Input types Error!",
           )
    assert PointToLine([1234.232, 1000], [10, 2],
                       decimal_point=-1).solve() == (
               None,
               "Input types Error!",
           )
