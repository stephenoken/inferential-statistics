from math import sqrt
from functools import reduce

with open("./finches.txt") as f:
    finches_data = [float(x) for x in f.readlines()]


def average(xs):
    return sum(xs) / len(xs)


def sample_standard_deviation(m, xs):
    return sqrt((1 / (len(xs) - 1) * reduce(lambda total, x: total + (x - m) ** 2, xs, 0.0)))


def t_test(m, s_e, x):
    return (x - m) / s_e


AVERAGE_BEAK_SIZE = round(average(finches_data), 2)
S_D = round(sample_standard_deviation(AVERAGE_BEAK_SIZE, finches_data), 2)
S_E = S_D / len(finches_data)
print(S_E)
T_SCORE = t_test(6.07, S_E, AVERAGE_BEAK_SIZE)
print("Finches Data")
print("Sample Size: {}".format(len(finches_data)))
print("Degress of Freedom {}".format(len(finches_data) - 1))
print("Average {}".format(AVERAGE_BEAK_SIZE))
print("Standard Deviation: {}".format(S_D))
print("T Test score: {}".format(T_SCORE))