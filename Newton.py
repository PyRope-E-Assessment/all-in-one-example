from random import randint
from scipy.special import lambertw

from pyrope import Exercise
from pyrope.nodes import Problem, Real

class Aufgabe(Exercise):

    def parameters(self):
        return {'y': randint(1, 10)}

    def problem(self, y):
        return Problem(r'''
            Lösen Sie die Gleichung
            $$
                 x\cdot e^x=<<y:latex>>
            $$
            näherungsweise mit Hilfe des Newton-Verfahrens unter Verwendung des Taschenrechners:\
            $x=$ <<x>>\
            Geben Sie das Ergebnis auf vier Stellen Genauigkeit an.
            ''',
            x = Real()
        )

    def the_solution(self, y):
        return lambertw(y)
    
    def hints(self):
        yield "Stellen Sie die Gleichung um."
        yield "$f(x) = x \cdot e^x - <<y:latex>>$."
        yield "$f'(x) = (x + 1)e^x$"
        yield (
            r"Nutzen Sie $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$, um eine Nullstelle mittels eines "
            r"Startwerts $x_0$ anzunähern."
        )
    
    def scores(self, x, y):
        return abs(x - lambertw(y)) <= 1e-4
    
    def feedback(self, x, y):
        if x is None:
            return ""
        if abs(x - lambertw(y)) <= 1e-4:
            return "Prima!"
        elif abs(x - lambertw(y)) <= 1e-1:
            return "Zu ungenau."
        else:
            return "Versuchs nochmal."
