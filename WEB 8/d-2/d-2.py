import json
from random import randrange
from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/member', methods=['GET'])
def member():
    data = json.load(open('templates/people.json'))['data']
    print(data)
    member = data[randrange(0, len(data))]
    print(member)
    member['prof'].sort()
    for k, v in member.items():
        print(k, v)
    return render_template('member.html', member=member)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
