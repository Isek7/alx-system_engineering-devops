#!/usr/bin/python3
'''
    for a given employee ID, returns information about
    his/her TODO list progress.
'''
import requests
import sys
# import logging


# logging.basicConfig(level=logging.DEBUG)
def get_username(user_id):
    '''Gets username of employee with user_id'''
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(user_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('name')


def get_todos(user_id):
    '''Retrieves todos of employee with user_id'''
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(todo_url)
    if response.status_code == 200:
        data = response.json()
        return data


def parse(username, todos):
    '''Parses data'''
    completed = []
    total_tasks = 0
    for todo in todos:
        total_tasks += 1
        if todo.get('completed') is True:
            completed.append(todo.get('title'))
    completed_tasks = len(completed)
    print(f"Employee {username} is done "
          f"with tasks({completed_tasks}/{total_tasks})")
    for task in completed:
        print(f"\t {task}")


if __name__ == '__main__':
    user_id = sys.argv[1]
    username = get_username(user_id)
    todos = get_todos(user_id)
    parse(username, todos)
