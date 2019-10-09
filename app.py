from flask import Flask
from bson.json_util import dumps
import requests
app = Flask(__name__)

SERVICE_KEY = 'NoFPviE7%2FZsmotCE8oolhUQbC%2Fwl8fnyN6MkOf9y90nnvUXnuAeMm0IXJ6O1YDNBGhetKPgNor2JqPiDZTIUYw%3D%3D'

app = Flask(__name__)


def parse_message(message):
    print(message)
    return message['DisasterMsg'][1]['row'][0]['msg']


def get_message():
    url = f'http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList?ServiceKey={SERVICE_KEY}&type=json&flag=Y'

    response = requests.get(url)
    return response


# 경로 설정, URL 설정
@app.route('/test', methods=['POST', 'GET'])
def index():
    message = get_message()
    print(f'message : {message}')
    return message.text


@app.route('/about')
def about():
    return 'About page'


@app.route('/')
def index():
    from database import db, conn
    cols = db.get_collection('disaster')

    # test = {'create_date': '2019-10-09', 'location_id': 136, 'message':'[서울] 경기 지역에서 돼지열병 발원 의심되오니 해당 지역 이동에 유념하시기 바랍니다.'}
    #
    # cols.insert(test)

    resp = dumps([x for x in cols.find()], ensure_ascii=False)
    print(resp)
    conn.close()

    return resp


if __name__ == '__main__':
    app.run()
