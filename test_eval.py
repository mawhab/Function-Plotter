import pytest
from pytestqt.qt_compat import qt_api
from eval import FunctionEvaluator
from Function_plotter import *

# test data for gui evaluation
# function, min, max, and expected status message
gui_test_data = [
        ('3x^2', '10', '20', r'Error: x needs to follow an operator 3x^2'),
        ('2*x+x^2+24*x+13', '-10', '-96', 'Error: Min value must be lower than max value.'),
        ('2^x+x^2+24*x+x', '-44', '84', 'Plotted 2^x+x^2+24*x+x'),
        ('X*13/7+32', '-58', 'a3', 'Error: Max value must be a number.'),
        ('13^2-16*x', '0a', '43', 'Error: Min value must be a number.'),
        ('7*X^2', '-89', '11', 'Plotted 7*X^2'),
        ('x9*2+17*x', '-87', '48', 'Error: A number needs to follow an operator or another number x9*2+17*x'),
        ('90*X-+17*x', '-60', '79', 'Error: An operator cannot follow an operator 90*X-+17*x'),
        ('214*a^2-17*x+1', '-82', '58', 'Error: x is the only alphabetic character allowed 214*a^2-17*x+1'),
        ('17+21*X^2+17*x', '-50', '44', 'Plotted 17+21*X^2+17*x')
    ]

# test data for function evaluation
# function and wether or not it's valid
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

# min max data
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

# evaluate function test data
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

# test function setting
# invalid functions should raise an assertion error
@pytest.mark.parametrize("fn, correctness", fn_test_data)
def test_set_f(fn, correctness):
    f = FunctionEvaluator()
    if correctness:
        f.set_function(fn)
        assert f.fn == fn and f.verifier.fn
    else:
        with pytest.raises(AssertionError):
            f.set_function(fn)

# test min max setting
# invalid min max combinations should raise an assertion error
@pytest.mark.parametrize("min, max", min_max_test_data)
def test_set_min_max(min,max):
    f = FunctionEvaluator()
    if min<max:
        f.set_min_max_val(min, max)
        assert f.verifier.min_val and f.verifier.max_val \
        and f.max_val==max and f.min_val==min
    else:
        with pytest.raises(AssertionError):
            f.set_min_max_val(min, max)

# test evaluation
# output should be similar to output caluclated by python
@pytest.mark.parametrize("fn,fn_correct, min, max", evaluate_test_data)
def test_evaluate(fn, fn_correct, min, max):
    f = FunctionEvaluator()
    f.set_function(fn)
    f.set_min_max_val(min,max)
    x,y = f.evaluate()
    assert (y==eval(fn_correct)).all()

# gui test
# status bar should print the correct message
@pytest.mark.parametrize("fn, min, max, msg", gui_test_data)
def test_gui(qtbot, fn, min, max, msg):
    win = MainWindow()
    qtbot.addWidget(win)
    win.ui.fx_input.insert(fn)
    win.ui.min_input.insert(min)
    win.ui.max_input.insert(max)
    qtbot.mouseClick(win.ui.plot_button, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert win.ui.status_output.toPlainText()==msg
