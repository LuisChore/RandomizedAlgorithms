'''
Vazquez Choreno Luis Ernesto
Randomized Algorithms
Application: Verifying Polynomial Identities


python3 PolynomialIdentity.py

'''
from random import seed
from random import randint


def evaluate_product_form(product_form,value):
    answer = 1
    for u in product_form:
        answer = (answer * (value + u))
    return answer




def evaluate_canonical_form(canonical_form,value):
    answer = 0
    canonical_form.reverse()
    v = 1
    for u in canonical_form:
        answer = answer + v*u
        v = value * v

    canonical_form.reverse()
    return answer



def get_rng(value):
    return randint(1,value)


#the chance that returns a wrong answer is no more than 1/n
def randomized_algorithm(product_form,canonical_form,degree):
    n = 100
    # choose a number between [1,n*degree]
    rng = get_rng(n*degree)
    # evaluate polynomials
    return (evaluate_product_form(product_form,rng) == evaluate_canonical_form(canonical_form,rng))


def main():
    seed(1)
    # (x + 1)(x − 2)(x + 3)(x − 4)(x + 5)(x − 6)
    product_form = [1,-2,3,-4,5,-6]
    #  x^6 − 7x^3 + 25
    canonical_form = [1,0,0,-7,0,0,25]


    # # (x + 1)(x + 2)
    # product_form = [1,2]
    # # x^2 + 3x + 2
    # canonical_form = [1,3,2]



    # repeating the algorithm with replacement k times
    same = True
    k = 10
    while k>0:
        k-=1
        same = same and randomized_algorithm(product_form,canonical_form,len(canonical_form) - 1)

    if same:
        print("Same polynomials")
    else:
        print("Different polynomials")


main()
