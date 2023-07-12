import string
import random
import pytest
from eval import Function_evaluator

@pytest.mark.parametrize("maybe_palindrome, expected_result", [
        ('2^x+x^2+24*x+13', True),
        ('2x+x^2+24*x+13', False),
        ('2^x+x^2+24*x+a', False),
        ('x*13/7+32', True),
        ('13^2-16x', False),
        ('7x^2', False),
        ('9*2+17*x', True),
        ('90*a-17*b', False),
        ('214*x^2-17*x+1', True),
        ('17+21x^2+17*x', True)
    ])
def test_set_f(fn, correctness):
    f = Function_evaluator()
    if not correctness:
        with pytest.raises(AssertionError):
            f.set_function()

def test_set_min_max(self):
    pass

def test_evaluate(self):
    pass

def test_cleanup(self):
    pass

def test_validate_fn(self):
    pass

def generate_cases():
    incorrect = []
    for _ in range(random.randint(1,100)): 
        incorrect.append(''.join(random.choices(string.ascii_uppercase \
                                + string.digits, k=random.randint(1,20))))
    correct = []
    for _ in range(random.randint(1,100)): 
        incorrect.append(''.join(random.choices(string.digits, 
                                k=random.randint(1,20))))
        
    return correct, incorrect