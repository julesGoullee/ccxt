# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.hitbtc import hitbtc


class dsx(hitbtc):

    def describe(self):
        return self.deep_extend(super(dsx, self).describe(), {
            'id': 'dsx',
            'name': 'DSX',
            'countries': ['UK'],
            'rateLimit': 100,
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/76909626-cb2bb100-68bc-11ea-99e0-28ba54f04792.jpg',
                'api': {
                    'public': 'https://api.dsxglobal.com',
                    'private': 'https://api.dsxglobal.com',
                },
                'www': 'http://dsxglobal.com',
                'doc': [
                    'https://api.dsxglobal.com',
                ],
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'maker': 0.15 / 100,
                    'taker': 0.25 / 100,
                },
            },
        })
