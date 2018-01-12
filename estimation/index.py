"""
    Lesson 2 Estimation calculations
"""
from math import sqrt
from functools import partial

with open("./engagement_ratio_data.txt") as f:
    ENGAGE_DATA = [float(x) for x in f.readlines()]
engae_mean = sum(ENGAGE_DATA) / len(ENGAGE_DATA)
s_d = sqrt((1. / len(ENGAGE_DATA)) * sum([(x - engae_mean)**2 for x in ENGAGE_DATA]))
standard_erorr_2 = s_d / sqrt(20)

def mean(xs):
    return sum(xs) / len(xs)


def x_score(m, o, z):
    return m + (o * z)


def standard_deviation(xs):
    m = mean(xs)
    return sqrt(1. / len(xs) * sum([(x - m)**2 for x in xs]))


def standard_erorr(sd, n):
    return sd / sqrt(n)


def confidence_intervals(m, o, z):
    _x_score = partial(x_score, m, o)
    return(round(_x_score(-z), 2), round(_x_score(z), 2))

def z_score(m, o, x):
    return (x - m) / o

def __secret():
    return "Uh-oh"


print "#######################"
print "Engagement Measurements"
print "#######################"
print "Mean : {}".format(mean(ENGAGE_DATA))
print "Standard Deviation: {}".format(standard_deviation(ENGAGE_DATA))
print "Standard Error: {}".format(standard_erorr(standard_deviation(ENGAGE_DATA), 20))
print "Confidence Interval: {}".format(confidence_intervals(.13, (.107 / sqrt(20)), 1.96))


print "#########################"
print "Measurement of Engagement"
print "Population"
print "M = 7.5 \t S_D = 0.64"
print "#########################"
print "Sample mean: 7.5"
print "Sample n: 20"
print "Sample s_d: {}".format(round(0.64 / sqrt(20), 3))
print "Z Score: {}".format(z_score(7.5, 0.14, 8.94))

print "#########################"
print "Measurement of Learning"
print "Population"
print "M = 8.2 \t S_D = 0.73"
print "#########################"
print "Sample mean: 8.2"
print "Sample n: 20"
print "Sample s_d: {}".format(round(0.73 / sqrt(20), 3))
print "Z Score: {}".format(z_score(8.2, 0.16, 8.35))

