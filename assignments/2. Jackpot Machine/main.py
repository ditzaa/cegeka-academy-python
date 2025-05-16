def return_jackpot(jackpot):
    jackpot = round(jackpot * 100)

    two_euros = jackpot // 200
    jackpot -= two_euros * 200

    one_euro = jackpot // 100
    jackpot -= one_euro * 100

    fifty_cents = jackpot // 50
    jackpot -= fifty_cents * 50

    twenty_cents = jackpot // 20
    jackpot -= twenty_cents * 20

    ten_cents = jackpot // 10
    jackpot -= ten_cents * 10

    five_cents = jackpot // 5
    jackpot -= five_cents * 5

    two_cents = jackpot // 2
    jackpot -= two_cents * 2

    one_cent = jackpot // 1
    jackpot -= one_cent * 1

    return (str(one_cent) + ", " + str(two_cents) + ", " + str(five_cents) + ", " + str(ten_cents) + ", "
            + str(twenty_cents) + ", " + str(fifty_cents) + ", " + str(one_euro) + ", "
            + str(two_euros))


# check solution
print(return_jackpot(8.01))
print(return_jackpot(19.99))
print(return_jackpot(37.88))
