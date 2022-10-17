#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her
TODO list progress in JSON format.
'''

if __name__ == '__main__':
    import json
    import requests
    import sys

    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    USER_ID = sys.argv[1]

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(USER_ID))
    name = user.json()
    username = name.get('username')

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(USER_ID))
    todos = req.json()

    json_dictionary = {}
    json_list = []

    for item in todos:
        json_dictionary['task'] = item.get('title')
        json_dictionary['completed'] = item.get('completed')
        json_dictionary['username'] = username
        json_list.append(json_dictionary)
        json_dictionary = {}

    json_return = {}
    json_return[USER_ID] = json_list

    with open(USER_ID + '.json', 'w') as json_file:
        json.dump(json_return, json_file)
