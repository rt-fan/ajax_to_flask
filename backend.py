import datetime
import time
import json

while True:
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    # print(time_now)
    with open('data.json', 'w', encoding='utf-8') as file:
        data = {}
        people = {}
        data['time'] = time_now
        people[1] = {'name': 'Первый'}
        people[2] = {'name': 'Второй'}
        people[3] = {'name': 'Третий'}
        data['people'] = people
        json.dump(data, file, ensure_ascii=False, indent=4)
    time.sleep(1)
