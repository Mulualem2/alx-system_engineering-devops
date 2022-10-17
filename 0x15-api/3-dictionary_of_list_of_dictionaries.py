#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her
TODO list progress in JSON format.
'''

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    url_task = 'https://jsonplaceholder.typicode.com/user/id/todos'
    users = requests.get(url).json()
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file:
        all_dict = {}
        for user in users:
            user_dict = {}
            tasks_list = []
            tasks = requests.get(url_task)
            for task in tasks:
                new_task_dict = {}
                new_task_dict["username"] = user.get('username')
                new_task_dict["task"] = task.get('title')
                new_task_dict["completed"] = task.get('completed')
                tasks_list.append(new_task_dict)
            all_dict[user.get('id')] = tasks_list
        json.dump(all_dict, file)
