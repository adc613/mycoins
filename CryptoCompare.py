import requests


class CryptoCompare(object):

    CC = "https://www.cryptocompare.com/api/"
    MIN_CC = "https://min-api.cryptocompare.com/"

    def get_coin_list(self):
        url = self.CC + 'data/coinlist'
        r = requests.get(url)
        return r.json()

    def get_coin_value(self, coin):
        url = self.MIN_CC + 'data/price'
        payload = {'fsym': coin, 'tsyms': 'USD'}
        r = requests.get(url, params=payload)
        data = r.json()
        return float(data["USD"])
