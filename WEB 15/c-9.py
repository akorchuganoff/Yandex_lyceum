import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
from flask import Flask, render_template

app = Flask(__name__)
LOGIN = '89021419881'
PASSWORD = '2111Efiop'

@app.route('/vk_stat/<int:group_id>')
def make_stats(group_id):
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.stats.get(group_id=group_id, stats_groups='activity', intervals_count=10)
    activity = [0, 0, 0]
    likes = 0
    comments = 0
    subscribed = 0
    ages = {
        '12-18': 0,
        '18-21': 0,
        '21-24': 0,
        '24-27': 0,
        '27-30': 0,
        '30-35': 0,
        '35-45': 0,
        '45-100': 0
    }
    cities = []
    if response:
        for i in response:
            print(i)
            if 'activity' in i.keys():
                if 'likes' in i['activity'].keys():
                    activity[0] += i['activity']['likes']
                if 'comments' in i['activity'].keys():
                    activity[1] += i['activity']['comments']
                if 'subscribed ' in i['activity'].keys():
                    activity[2] += i['activity']['subscribed ']
            if 'age' in i['reach']:
                for elem in i['reach']['age']:
                    ages[elem['value']] += elem['count']
            if 'cities' in i['reach'].keys():
                print(1)
                for elem in i['reach']['cities']:
                    if elem['name'] not in cities:
                        cities.append(elem['name'])

    print(cities)

    return render_template('index.html', activity=activity, ages=ages, cities=cities)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)