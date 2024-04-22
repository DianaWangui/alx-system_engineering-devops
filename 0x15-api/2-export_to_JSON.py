#!/usr/bin/python3

""" employee to do to csv """

import json
import requests
import sys


if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    employee_name = ''
    data = {}
    list_1 = []

    for user in users.json():
        if user.get('id') == int(sys.argv[1]):
            employee_name = user.get('username')
    for todo in todos.json():
        if todo.get('userId') == int(sys.argv[1]):
            list_1.append({
               "task": todo.get("title"),
               "completed": todo.get("completed"),
               "username": employee_name
            })
    data.update({sys.argv[1]: list_1})

    filename = f'{sys.argv[1]}.json'
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)
