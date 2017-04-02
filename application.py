from flask import Flask, request
import requests

"""
configure your PostmarkApp token, to and from address here
the from address needs to be verified with postmark, otherwise it'll fail
"""
token = 'your-postmark-token'
toAddress = 'to@example.com'
fromAddress = 'from@example.com'


url = 'https://api.postmarkapp.com/email'

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def receive():
    if request.method == 'POST':
        data = request.get_json()
        msgFrom = data['from']
        msgTo = data['to']
        msgBody = data['text']

        subject = "New SMS from %s" % (msgFrom)

        payload = {'From': fromAddress, 'To': toAddress, 'Subject': subject, 'Textbody': msgBody}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'X-Postmark-Server-Token': token}
        req = requests.post(url, json=payload, headers=headers)

        if req.status_code == 200:
            return '', 200
        else:
            return req.text
    else:
        return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
