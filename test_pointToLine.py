from pointToLine import point_to_line
import pytest
import math


@pytest.mark.regular
def test_point_to_line_int():
    assert point_to_line([1, 1],
                         [2, 2]) == (
               "(-1.000) * X + (1.000) * Y = 0.000", None)
    assert point_to_line([1, 2],
                         [2, 2]) == (
               "1.000 * Y = 2.000 with A = 0", None)
    assert point_to_line([0, 0],
                         [2, -7]) == (
               "(7.000) * X + (2.000) * Y = 0.000", None)


@pytest.mark.regular
def test_point_to_line_float():
    assert point_to_line([1.367123, 1.7263487],
                         [2.276492, 6.737453], decimal_point=10) == (
               "(-5.0111043000) * X + (0.9093690000) * Y = -5.2809079530",
               None)
    assert point_to_line([1.23, 2],
                         [2.78, 2]) == (
               "1.550 * Y = 3.100 with A = 0", None)
    assert point_to_line([1234.232, 1000],
                         [10, 2], decimal_point=3) == (
               "(998.000) * X + (-1224.232) * Y = 7531.536", None)


@pytest.mark.error
def test_point_to_line_same():
    assert point_to_line([1, 1], [1, 1]) == (
        None, "Please input two different points!"
    )
    assert point_to_line([0, 0], [0, 0]) == (
        None, "Please input two different points!"
    )
    assert point_to_line([1000, 1000], [1000, 1000]) == (
        None, "Please input two different points!"
    )


@pytest.mark.error
def test_point_to_line_inf():
    assert point_to_line([math.inf, 1000], [1000, 1000]) == (
        None, "Yours inputs for should be less than Infinity!")
    assert point_to_line([-6427384, 1000], [1000, math.inf]) == (
        None, "Yours inputs for should be less than Infinity!")
    assert point_to_line([-6427328973428937423484, 1000],
                         [1000, math.inf]) == (
               None, "Yours inputs for should be less than Infinity!")


@pytest.mark.error
def test_point_to_line_input_type():
    assert point_to_line(['asd', 1000],
                         [10, 20.234]) == (
               None, "Make sure your inputs are numerical!")
    assert point_to_line([1234.232, 1000],
                         [10, "dsfaw"]) == (
               None, "Make sure your inputs are numerical!")


@pytest.mark.error
def test_point_to_line_decimal():
    assert point_to_line([1234.232, 1000],
                         [10, 2], decimal_point=1.3) == (
               None, "Input types Error!")
    assert point_to_line([1234.232, 1000],
                         [10, 2], decimal_point=-1.3) == (
               None, "Input types Error!")
    assert point_to_line([1234.232, 1000],
                         [10, 2], decimal_point=-1) == (
               None, "Input types Error!")

