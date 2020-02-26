'''
Vazquez Choreno Luis Ernesto
Randomized Algorithms
Application: Example Coupon Collectors Problem


python3 Coupon.py
'''

from random import seed
from random import randint
import matplotlib.pyplot as plt
import numpy as np
def get_rng(value):
    return np.random.randint(low=1, high=value+1)



def randomized_algorithm(num_coupons):
    collector  = []
    for i in range(0,num_coupons+1):
        collector.append(False)
    counter = 0
    iteration = 0
    while counter < num_coupons:
        iteration += 1
        rng = int(get_rng(num_coupons))
        if collector[rng] == True:
            continue
        else:
            collector[rng] = True
            counter+=1
    return iteration



def save_plot(x,expectedY,practiceY,name):
    plt.plot(x,expectedY, label='Valor esperado')
    plt.plot(x,practiceY, label ='Algoritmo Aleatorio')
    plt.legend(framealpha=1, frameon=True);
    plt.ylabel("Intentos hasta obtener c cupones")
    plt.xlabel('c cupones')
    #plt.savefig(name)
    plt.show()

def main():
    num_coupons = 100

    print("Expected value: " +  str(num_coupons * np.log(num_coupons) + num_coupons))
    print("Practice " + str(randomized_algorithm(num_coupons)))

    x = []
    expectedY = []
    practiceY = []
    for i in range(1,num_coupons + 1,5):
        expectedY.append(i * np.log(i) + i)
        practiceY.append(randomized_algorithm(i))
        x.append(i)
    save_plot(x,expectedY,practiceY,"Plots/PythonFile.png")

main()
