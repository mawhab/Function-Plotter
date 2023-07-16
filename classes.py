from typing import List

class Term:
    def __init__(self, term:str) -> None:
        self.term = term
        self.x_term = False
        self.x_in_dem = False
        self.fraction = False
        self.numerator = 1
        self.denomenator = 1
        self.num_power = 1
        self.denom_power = 1
    
    def eval(self, x:List[float]=None) -> List[float]:
        pass

    def check_all(self):
        pass

    def check_x(self):
        if 'x' in self.term or 'X' in self.term:
            self.x_term = True
    def check_denom(self):
        if '/' in self.term:
            term = self.term.split('/')[1]
            if 'x' in term or 'X' in term:
                self.x_in_dem = True
        else:
            self.fraction = False
class Function:
    def __init__(self, f:str) -> None:
        self.f = f
        self.terms = Function.extract_terms(f)
    
    def eval(self, x:List[float]) -> List[float]:
        total = 0
        for term in self.terms:
            total+=term.eval()
        return total

    def extract_terms(f:str) -> List[str]:
        terms = f.split('+')
        to_rem = []
        for i, term in enumerate(terms):
            if '-' in term:
                start = True
                for neg_term in term.split('-'):
                    if start:
                        start = False
                    else:
                        neg_term = '-' + neg_term
                    terms.append(neg_term)
                to_rem.append(i)
        to_rem.reverse()
        for t in to_rem:
            del terms[t]
        
        return [Term(term) for term in terms]
