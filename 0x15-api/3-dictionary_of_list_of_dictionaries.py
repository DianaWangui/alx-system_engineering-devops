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

    for user in users.json():
        list_1 = []
        for todo in todos.json():
            employee_name = user.get('username')
            list_1.append({
                "username": employee_name,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })

        data.update({user.get('id'): list_1})

    filename = 'todo_all_employees.json'
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)
