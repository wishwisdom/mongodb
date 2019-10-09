import unittest

import requests

SERVICE_KEY = 'NoFPviE7%2FZsmotCE8oolhUQbC%2Fwl8fnyN6MkOf9y90nnvUXnuAeMm0IXJ6O1YDNBGhetKPgNor2JqPiDZTIUYw%3D%3D'


def parse_message(message):
    print(message)
    return message['DisasterMsg'][1]['row'][0]['msg']


def get_message():
    url = f'http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList?ServiceKey={SERVICE_KEY}&type=json&flag=Y'
    params = {
        #'ServiceKey': SERVICE_KEY,
        'pageNo': 1,
        'numOfRows': 1,
        'type': 'json',
        'flag': 'Y'
    }

    response = requests.get(url)
    print(response)
    return response


class MyTestCase(unittest.TestCase):
    def test_something(self):
        message = get_message()
        print(message.text)
        msg = parse_message(message)



if __name__ == '__main__':
    unittest.main()
