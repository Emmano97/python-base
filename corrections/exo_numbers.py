
from nbautoeval import Args, ExerciseFunction

from random import randint

# @BEG@ name=numbers
def numbers(*liste):
    """
    retourne un tuple contenant
    (*) la somme
    (*) le minimum
    (*) le maximum
    des éléments de la liste
    """

    if not liste:
        return 0, 0, 0

    return (
        # la builtin 'sum' renvoie la somme
        sum(liste),
        # les builtin 'min' et 'max' font ce qu'on veut aussi
        min(liste),
        max(liste),
    )
# @END@


# @BEG@ name=numbers more=bis
# en regardant bien la documentation de sum, max et min,
# on voit qu'on peut aussi traiter le cas singulier
# (où il n'y pas d'argument) en passant
#   start à sum
#   et default à min ou max
# comme ceci
def numbers_bis(*liste):
    return (
        # attention, la signature de sum est:
        #   sum(iterable[, start])
        # du coup on ne PEUT PAS passer à sum start=0
        # parce que start n'a pas de valeur par défaut
        # on pourrait par contre faire juste sum(liste)
        # car le défaut pour start c'est 0
        # dit autrement, sum([]) retourne bien 0
        sum(liste, 0),
        # par contre avec min c'est
        #  min(iterable, *[, key, default])
        # du coup on DOIT appeler min avec default=0 qui est plus clair
        # l'étoile qui apparaît dans la signature
        # rend le paramètre default keyword-only
        min(liste, default=0),
        max(liste, default=0),
    )
# @END@


def numbers_ko(liste):
    return (
        # la builtin 'sum' renvoie la somme
        sum(liste),
        # les builtin 'min' et 'max' font ce qu'on veut aussi
        max(liste),
        min(liste),
    )


def numbers_input():
    length = randint(2, 6)
    result = []
    for _ in range(length):
        result.append(randint(5, 15))
    return result


numbers_inputs = [Args(), Args(6)] + [Args(*numbers_input()) for i in range (4)]

exo_numbers = ExerciseFunction(
    numbers, numbers_inputs,
    nb_examples = 3,
)

