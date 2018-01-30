from math import sqrt

def z_score(m, o, x):
    return (x - m) / o


def mean(xs):
    return sum(xs) / len(xs)


def s_d(m, xs):
    return sqrt((1. / len(xs)) * reduce(lambda prev, x: prev + (x - m) ** 2, xs, 0))


if __name__ == "__main__":
    with open("./estimations.txt") as f:
        data = [float(l) for l in f.readlines()]
        print mean(data)
        print s_d(mean(data), data)

        print z_score(7.47, (2.41 / sqrt(30)), 8.3)
        print z_score(7.47, (2.41 / sqrt(50)), 8.3)

        print z_score(7.47, (2.41 / sqrt(30)), 7.8)
        print z_score(7.47, (2.41 / sqrt(50)), 7.8)
