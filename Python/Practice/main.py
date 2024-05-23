import time
import cProfile
import pstats


def Add(x, y):
    resultingSum = 0
    resultingSum += x
    resultingSum += y
    return resultingSum


def DoStuff():
    result = []

    for x in range(100000):
        result.append(x**2)
    return result


def WasteTime():
    time.sleep(3)
    print("done sleeping")


if __name__ == "__main__":
    with cProfile.Profile() as profile:
        print(Add(100, 500))
        print(DoStuff())
        WasteTime()

        results = pstats.Stats(profile)
        results.sort_stats(pstats.SortKey.TIME)
        results.print_stats()
