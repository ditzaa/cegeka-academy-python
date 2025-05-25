import sys


def return_jackpot_improved(*jackpots):
    """

    :param jackpots: list of amounts won at the slot machine
    :return: list of tuples representing each jackpot returned according to the required denomination
    """
    results = []
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    for jackpot in jackpots:
        jackpot_in_cents = round(jackpot * 100)
        jackpot_in_coins = []
        for denomination in denominations:
            nb_of_coins = jackpot_in_cents // denomination
            jackpot_in_coins.insert(0, nb_of_coins)
            jackpot_in_cents -= denomination * nb_of_coins

        coins = tuple(jackpot_in_coins)
        results.append(coins)

    return results


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        arguments = [float(argument) for argument in sys.argv[1:]]
        print(return_jackpot_improved(*arguments))

# function testing
# print(return_jackpot_improved())
# print(return_jackpot_improved(8.01))
# print(return_jackpot_improved(8.01, 19.99, 37.88))
