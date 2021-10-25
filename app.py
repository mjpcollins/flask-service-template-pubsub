from flask import Flask, request
from config.conf import settings
from utils.pubsub import pubsub_message_to_dict
app = Flask(__name__)


@app.route('/')
def home():
    return 'OK'


@app.route("/pubsub", methods=["POST"])
def pubsub():
    envelope = request.get_json()
    message_data, err_code = pubsub_message_to_dict(envelope)
    print(f'envelope: {envelope} -- message_data: {message_data} -- err_code: {err_code}')
    if err_code >= 300:
        return message_data, err_code
    return message_data, err_code


def run():
    app.run(host='0.0.0.0',
            port=settings['port'])


def debug():
    app.run(host='0.0.0.0',
            port='5000')


if __name__ == '__main__':
    run()
