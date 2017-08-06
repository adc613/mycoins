from CryptoCompare import CryptoCompare


class Prompt():

    def __init__(self):
        self.cc = CryptoCompare()
        self.coins = None

    def list_coins(self):
        if self.coins is None:
            self.coins = self.cc.get_coin_list()['Data']

        for key in self.coins.keys():
            full_name = self.coins[key]['FullName']
            name = self.coins[key]['Name']
            msg = "[{}] {} :".format(name, full_name)
            print(msg)

    def ask_user_for_list(self):
        should_list = input("do you need a list of coins? [Y/N] ->\n").lower() \
            == 'y'
        if should_list:
            self.list_coins()

    def ask_user_for_coins(self):
        coins = []
        while True:
            coin = input("What is the coin ticker? [Enter ends loop]-> \n") \
                .strip() \
                .upper()

            if coin == '':
                break
            amount = float(input("How many coins do you own? -> \n"))
            coins.append((coin, amount))

        return coins


def main():
    prompt = Prompt()
    prompt.ask_user_for_list()
    coins = prompt.ask_user_for_coins()

    sum = 0.0
    totals = {}
    for (coin, amount) in coins:
        value = prompt.cc.get_coin_value(coin)
        amount = value * amount
        if coin in totals:
            totals[coin] += amount
        else:
            totals[coin] = amount
        sum += amount
        print("{} is at ${} per coin".format(coin, value, amount))

    for coin in totals.keys():
        percentage = (totals[coin] / sum) * 100
        print("You own ${} of {} at {}% of your protfolio"
              .format(totals[coin], coin, percentage))

    print("Your total portfolio is valued at ${}".format(sum))

if __name__ == "__main__":
    main()
