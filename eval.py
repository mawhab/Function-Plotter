import numpy as np

class Function_evaluator:
    def __init__(self, num_points:int=10000) -> None:
        self.num_points = num_points
        self.verifier = Function_evaluator.Verifer()

    def set_function(self,f):
        res = Function_evaluator.validate_fn(f)
        assert res.passed, res.full_msg
        self.verifier.fn = True
        self.fn = f

    def set_min_max_val(self, min_val, max_val):
        assert min_val<max_val, 'Min value must be lower than max value.'
        try:
            self.min_val = float(min_val)
            self.verifier.min_val = True
        except ValueError:
            raise AssertionError('Min value must be a number.')
        
        try:
            self.max_val = float(max_val)
            self.verifier.max_val = True
        except ValueError:
            raise AssertionError('Max value must be a number.')

    def evaluate(self):
        assert self.verifier.fn and self.verifier.max_val and self.verifier.min_val, 'One or more parameters has not been verified'
        self.fn = Function_evaluator.cleanup_fn(self.fn)
        x = np.linspace(self.min_val, self.max_val, self.num_points)
        y = eval(self.fn)
        return x,y

        
    def cleanup_fn(f:str) -> str:
        f = f.replace('^', '**')
        f = f.replace('X', 'x')
        return f
    
    def validate_fn(f:str):
        prev=''
        err_start = 0
        OPERATORS = ['+', '-', '*', '/', '^', '']
        for i,c in enumerate(f):
            if c.isdigit():
                if not (prev.isdigit() or prev in OPERATORS):
                    return Function_evaluator.Function_error(f, False, 'A number needs to follow an operator or another number', err_start, i)
                elif not prev.isdigit():
                    err_start=i
            else:
                if c in OPERATORS:
                    if prev in OPERATORS:
                        return Function_evaluator.Function_error(f, False, 'An operator cannot follow an operator', i)
                elif c=='x' or c=='X':
                    if not (prev in OPERATORS):
                        return Function_evaluator.Function_error(f, False, 'x needs to follow an operator', err_start, i)
                elif c.isalpha():
                        return Function_evaluator.Function_error(f, False, 'x is the only alphabetic character allowed', err_start, i)
            prev = c
        return Function_evaluator.Function_error(f,True, None, None, None)
    
    class Verifer:
        def __init__(self) -> None:
            self.fn = False
            self.min_val = False
            self.max_val = False

    class Function_error:
        # end = '\033[0m'
        # underline = '\033[4m'
        end = '</u>'
        underline = '<u>'
        def __init__(self, f, passed, error, start, end=None) -> None:
            self.passed = passed
            if not passed:
                self.error_msg = error
                self.start = start
                self.end = end if end else start+1
                self.line = f[:self.start] + Function_evaluator.Function_error.underline \
                + f[self.start:self.end+1] + Function_evaluator.Function_error.end + f[self.end+1:]
                self.full_msg = 'Error: ' + self.error_msg + ' ' + self.line

        def __eq__(self, __value: object) -> bool:
            return self.full_msg == __value.full_msg