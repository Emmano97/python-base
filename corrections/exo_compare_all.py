
from nbautoeval import Args, ExerciseFunction, CallRenderer

from functools import reduce


# @BEG@ name=compare_all
def compare_all(fun1, fun2, entrees):
    """
    retourne une liste de booléens, un par entree dans entrees
    qui indique si fun1(entree) == fun2(entree)
    """
    # on vérifie pour chaque entrée si f et g retournent
    # des résultats égaux avec ==
    # et on assemble le tout avec une comprehension de liste
    return [fun1(entree) == fun2(entree) for entree in entrees]
# @END@



compare_all_inputs = []

# factoriel
from operator import mul
def fact(n):
    "une version de factoriel à base de reduce"
    return reduce(mul, range(1, n+1), 1)
from math import factorial
fact_inputs = [0, 1, 5]

compare_all_inputs.append(Args(fact, factorial, fact_inputs))

def broken_fact(n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

compare_all_inputs.append(Args(broken_fact, factorial, fact_inputs))

#################### the exercice instance
exo_compare_all = ExerciseFunction(
    compare_all, compare_all_inputs,
    nb_examples = 2,
    call_renderer=CallRenderer(show_function=False),
)


def compare_all_ko(*args):
    return [not x for x in compare_all(*args)]

