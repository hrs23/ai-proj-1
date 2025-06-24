import os
import json
import argparse
import time

TASKS_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    print(f"Added task: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks.')
        return
    for idx, task in enumerate(tasks, 1):
        status = 'X' if task.get('completed') else ' '
        print(f"[{status}] {idx}: {task.get('description')}")


def complete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index-1]['completed'] = True
        save_tasks(tasks)
        print(f"Completed task: {tasks[index-1]['description']}")
    else:
        print('Invalid task number.')


def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        task = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Removed task: {task['description']}")
    else:
        print('Invalid task number.')


def pomodoro(index, work=25, rest=5):
    tasks = load_tasks()
    if not (1 <= index <= len(tasks)):
        print('Invalid task number.')
        return
    task = tasks[index-1]
    print(f"Starting Pomodoro for task: {task['description']}")
    for minute in range(work, 0, -1):
        print(f"Work: {minute} minute(s) remaining...")
        time.sleep(60)
    print('Work period complete! Time for a break.')
    for minute in range(rest, 0, -1):
        print(f"Break: {minute} minute(s) remaining...")
        time.sleep(60)
    print('Break over! Good job!')


def main():
    parser = argparse.ArgumentParser(description='Simple TODO app with Pomodoro')
    subparsers = parser.add_subparsers(dest='command')

    add_p = subparsers.add_parser('add', help='Add a new task')
    add_p.add_argument('description', help='Task description')

    list_p = subparsers.add_parser('list', help='List tasks')

    done_p = subparsers.add_parser('done', help='Mark task as completed')
    done_p.add_argument('index', type=int, help='Task number')

    rm_p = subparsers.add_parser('remove', help='Remove a task')
    rm_p.add_argument('index', type=int, help='Task number')

    pomo_p = subparsers.add_parser('pomodoro', help='Start Pomodoro for a task')
    pomo_p.add_argument('index', type=int, help='Task number')
    pomo_p.add_argument('--work', type=int, default=25, help='Work minutes')
    pomo_p.add_argument('--rest', type=int, default=5, help='Break minutes')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'done':
        complete_task(args.index)
    elif args.command == 'remove':
        remove_task(args.index)
    elif args.command == 'pomodoro':
        pomodoro(args.index, args.work, args.rest)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
