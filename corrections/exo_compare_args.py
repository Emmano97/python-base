
from nbautoeval import Args, ExerciseFunction, CallRenderer


# @BEG@ name=compare_args
def compare_args(fun1, fun2, arg_tuples):
    """
    retourne une liste de booléens, un par entree dans entrees
    qui indique si fun1(*tuple) == fun2(*tuple)
    """
    # c'est presque exactement comme compare_all, sauf qu'on s'attend
    # à recevoir une liste de tuples d'arguments, qu'on applique
    # aux deux fonctions avec la forme * au lieu de les passer directement
    return [fun1(*arg) == fun2(*arg) for arg in arg_tuples]
# @END@


#################### les jeux de données
compare_args_inputs = []

from functools import reduce
from math import factorial
from operator import add, mul

########## dataset #1
fact_inputs = [(0,), (1,), (5,),]

def broken_fact(n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

compare_args_inputs.append(Args(broken_fact, factorial, fact_inputs))

########## dataset #2
# addition can work too
add_inputs = [(2, 3), (0, 4), (4, 5)]

def plus_broken(x1, x2):
    if x1 != 0:
        return x1 + x2
    else:
        return 1 + x2

compare_args_inputs.append(Args(add, plus_broken, add_inputs))

########## dataset #3
# factoriel is still valid

def fact(n):
    "une version de factoriel à base de reduce"
    return reduce(mul, range(1, n+1), 1)

compare_args_inputs.append(Args(fact, factorial, fact_inputs))

########## dataset #4

def plus(x1, x2):
    return x1 + x2

compare_args_inputs.append(Args(add, plus, add_inputs))

#################### the exercise instance
exo_compare_args = ExerciseFunction(
    compare_args, compare_args_inputs,
    nb_examples=2,
    call_renderer=CallRenderer(show_function=False),
    font_size='x-small',
)


def compare_args_ko(*args, **keywords):
    return [not x for x in compare_args(*args, **keywords)]

