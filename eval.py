import numpy as np

class FunctionEvaluator:
    def __init__(self, num_points:int=10000) -> None:
        '''
        Initialise the class. Sets the default number of points to evaluate (x). 
        Creates verifer object to test input function.

        num_points: (int) The precision of the evaluation. Used later in generating x with min and max values.

        Returns: None

        Raises:
            None
        '''
        self.num_points = num_points
        self.verifier = FunctionEvaluator.Verifer()

    def set_function(self,f:str):
        '''
        Takes a function as a string, validates it for syntax errors. If it has
        no errors, it is set as the function and flagged as verified. Otherwise
        an assertion error is raised.

        f: (str) function to be evaluated.

        Returns: None

        Raises: 
            Assertion error: If function is not valid or contains syntax errors.
        '''
        res = FunctionEvaluator.validate_fn(f)
        assert res.passed, res.full_msg
        self.verifier.fn = True
        self.fn = f

    def set_min_max_val(self, min_val:float, max_val:float):
        '''
        Verifies and sets min and max values for the evaluation (x). Min and 
        max values are checked to make sure they are numbers then they are checked
        to make sure min is lower than max. If any of the checks fail, an assertion
        error is raised with the appropriate message.

        min_val: (float) Starting point to generate x from.
        max_val: (float) End point to generate x to.

        Returns: None

        Raises:
            Assertion error: If either min_val or max_val is not float or int, or if min_val<max_val.
        '''
        try:
            min_val = float(min_val)
        except ValueError:
            raise AssertionError('Error: Min value must be a number.')
        self.min_val = min_val
        self.verifier.min_val = True

        try:
            max_val = float(max_val)
        except ValueError:
            raise AssertionError('Error: Max value must be a number.')
        self.max_val = max_val
        self.verifier.max_val = True
        
        assert min_val<max_val, 'Error: Min value must be lower than max value.'

    def evaluate(self) -> tuple:
        '''
        Main evaluation function. First, all inputs are checked to make sure they have been verified.
        Otherwise, an assertion error is raised. Then the input fn is cleaned up to fit python's syntax.
        Then we utilize python's built in eval function to evaluate the function.

        Returns: (tuple) x,y evaluated from the setup function.

        Raises:
            Assertion error: If set up has not been completed. Input function, min val, max val is missing.
        '''
        assert self.verifier.fn and self.verifier.max_val and self.verifier.min_val, 'One or more parameters has not been verified'
        self.fn = FunctionEvaluator.cleanup_fn(self.fn)
        x = np.linspace(self.min_val, self.max_val, self.num_points)
        y = eval(self.fn)
        return x,y

        
    def cleanup_fn(f:str) -> str:
        '''
        Replaces uppercase x with lowercase x and replaces (^) with ** to match python's syntax.

        f: (str) Function to clean.

        Returns: (str) f clean function

        Raises: None
        '''
        f = f.replace('^', '**')
        f = f.replace('X', 'x')
        return f
    
    def validate_fn(f:str):
        '''
        Iterates through the given function to check for syntax errors.
        Syntax errors include: 
            - Number following x. e.g.: x2. Correct: x*2.
            - X following number. e.g.: 2x. Correct: 2*x.
            - Consecutive operators. e.g.: x++3. Correct: x++3.
            - Non numeric character other than x. e.g.: 2*a. Correct: 2*x.

        f: (str) Function to validate.

        Returns: (FunctionEvaluator) FunctionEvaluator object that contains evaluation information

        Raises: None
        '''
        prev=''
        err_start = 0
        OPERATORS = ['+', '-', '*', '/', '^', '']
        for i,c in enumerate(f):
            if c.isdigit():
                if not (prev.isdigit() or prev in OPERATORS):
                    return FunctionEvaluator.Function_error(f, False, 'A number needs to follow an operator or another number', err_start, i)
                elif not prev.isdigit():
                    err_start=i
            else:
                if c in OPERATORS:
                    if prev in OPERATORS:
                        return FunctionEvaluator.Function_error(f, False, 'An operator cannot follow an operator', i)
                elif c=='x' or c=='X':
                    if not (prev in OPERATORS):
                        return FunctionEvaluator.Function_error(f, False, 'x needs to follow an operator', err_start, i)
                elif not c.isdigit() and not (c=='x' or c=='X'):
                        return FunctionEvaluator.Function_error(f, False, 'x is the only alphabetic character allowed', err_start, i)
            prev = c
        return FunctionEvaluator.Function_error(f,True, None, None, None)
    
    class Verifer:
        '''
        Inner class to hold verified data info
        '''
        def __init__(self) -> None:
            self.fn = False
            self.min_val = False
            self.max_val = False

    class Function_error:
        '''
        Inner class to hold function validation info
        '''
        end = '</u>'
        underline = '<u>'
        def __init__(self, f, passed, error, start, end=None) -> None:
            self.passed = passed # whether or not the function is valid
            if not passed: # if not valid construct error message
                self.error_msg = error # error generated in validation
                self.start = start # start of substring containing error
                self.end = end if end else start+1 # end of substring containing error

                # creating error message + underlined error
                self.line = f[:self.start] + FunctionEvaluator.Function_error.underline \
                + f[self.start:self.end+1] + FunctionEvaluator.Function_error.end + f[self.end+1:]
                self.full_msg = 'Error: ' + self.error_msg + ' ' + self.line