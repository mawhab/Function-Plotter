import string
import random
import pytest
import numpy as np
from eval import Function_evaluator

fn_test_data = [
        ('2^x+x^2+24*x+13', True),
        ('2x+x^2+24*x+13', False),
        ('2^x+x^2+24*x+a', False),
        ('x*13/7+32', True),
        ('13^2-16x', False),
        ('7x^2', False),
        ('9*2+17*x', True),
        ('90*a-17*b', False),
        ('214*x^2-17*x+1', True),
        ('17+21x^2+17*x', False)
    ]

min_max_test_data = [
        (10,20),
        (24,93),
        (97,-3),
        (-68,13),
        (70,94),
        (-95,80),
        (26,24),
        (-56,-76),
        (-64,-69),
        (-51,-11)
    ]
evaluate_test_data = [
        ('x^2','x**2', 10,20),
        ('2*x+x^2+24*x+13','2*x+x**2+24*x+13', -10,96),
        ('2^x+x^2+24*x+x','2**x+x**2+24*x+x', -44,84),
        ('X*13/7+32','x*13/7+32', -58,93),
        ('13^2-16*x','13**2-16*x', 0,43),
        ('7*X^2','7*x**2', -89,11),
        ('9*2+17*x','9*2+17*x', -87,48),
        ('90*X-17*x','90*x-17*x', -60,79),
        ('214*x^2-17*x+1','214*x**2-17*x+1', -82,58),
        ('17+21*X^2+17*x','17+21*x**2+17*x', -50,44)
    ]

validate_test_data = [
        (10,20, True),
        (24,93, True),
        (97,-3, True),
        (-68,13, True),
        (10,20, True),
        (10,20, True),
        (10,20, True),
        (10,20, True),
        (10,20, True),
        (10,20, True)
    ]

@pytest.mark.parametrize("fn, correctness", fn_test_data)
def test_set_f(fn, correctness):
    f = Function_evaluator()
    if correctness:
        f.set_function(fn)
        assert f.fn == fn and f.verifier.fn
    else:
        with pytest.raises(AssertionError):
            f.set_function(fn)

@pytest.mark.parametrize("min, max", min_max_test_data)
def test_set_min_max(min,max):
    f = Function_evaluator()
    if min<max:
        f.set_min_max_val(min, max)
        assert f.verifier.min_val and f.verifier.max_val \
        and f.max_val==max and f.min_val==min
    else:
        with pytest.raises(AssertionError):
            f.set_min_max_val(min, max)

@pytest.mark.parametrize("fn,fn_correct, min, max", evaluate_test_data)
def test_evaluate(fn, fn_correct, min, max):
    f = Function_evaluator()
    f.set_function(fn)
    f.set_min_max_val(min,max)
    x,y = f.evaluate()
    assert (y==eval(fn_correct)).all()
