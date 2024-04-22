#!/usr/bin/python3

""" employee to do to csv """

import requests
import sys


if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    employee_name = ''
    csv = []

    for user in users.json():
        if user.get('id') == int(sys.argv[1]):
            employee_name = user.get('username')
    for todo in todos.json():
        if todo.get('userId') == int(sys.argv[1]):
            csv.append(
                f'"{sys.argv[1]}","{employee_name}",'
                f'"{todo.get("completed")}",'
                f'"{todo.get("title")}"'
            )

    filename = f'{sys.argv[1]}.csv'
    with open(filename, mode='w', newline='') as file:
        for row in csv:
            file.write(row + '\n')
