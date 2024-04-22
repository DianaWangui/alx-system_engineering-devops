#!/usr/bin/python3

""" employee to do """

import requests
import sys


if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    employee_name = ''
    number_of_done_tasks = 0
    tototal_number_of_task = 0
    task_title = []

    for user in users.json():
        if user.get('id') == int(sys.argv[1]):
            employee_name = user.get('name')
    for todo in todos.json():
        if todo.get('userId') == int(sys.argv[1]):
            tototal_number_of_task += 1
            if todo.get('completed') is True:
                number_of_done_tasks += 1
                task_title.append(todo.get('title'))
    print(f'Employee {employee_name} is done with tasks'
          f'({number_of_done_tasks}/{tototal_number_of_task}):')
    for title in task_title:
        print(f'\t {title}')
