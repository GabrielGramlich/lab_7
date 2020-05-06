import requests

def main():
    value = get_BTC_value()
    display_BTC_value(value)


def get_BTC_value():
	data = get_current_BTC_data()
	value = data['bpi']['USD']['rate_float']
	return value


def get_current_BTC_data():
	''' Originally this method was on it's own, called from main outside of get_BTC_value so it didn't
	 have to be mocked in the tests, but if I read the labs right, it was supposed to be structured
	 this way. Not really sure, but I feel like it's better to just leave it in it's own method and
	 send the data returned by this to get_BTC_value for the sake of testing and adaptability, but it's
	 a super simple program, so yeah, structured it like this for the sake of the lab description.
	'''
	data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
	return data


def display_BTC_value(value):
    print(f'1 bitcoin is equivalent to ${round(value, 2)}')


if __name__ == '__main__':
    main()
