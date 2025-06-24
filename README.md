# ai-proj-1

## Usage

This repository contains a simple TODO application with a built-in Pomodoro timer.

### Adding a task

```bash
python todo.py add "Write documentation"
```

### Listing tasks

```bash
python todo.py list
```

### Marking a task as completed

```bash
python todo.py done 1
```

### Removing a task

```bash
python todo.py remove 1
```

### Starting a Pomodoro session

The default Pomodoro is 25 minutes of work followed by a 5 minute break. You can
adjust these times with the `--work` and `--rest` options (values are minutes).

```bash
python todo.py pomodoro 1 --work 25 --rest 5
```

## Web App (TypeScript)

This project also provides a simple Express-based web API written in TypeScript.

### Installation

```bash
npm install
```

### Development mode

```bash
npm run dev
```

### Build and run

```bash
npm run build
npm start
```

The server exposes the following endpoints:

- `GET /tasks` - list all tasks
- `POST /tasks` - add a new task (JSON body `{ "description": "..." }`)
- `PUT /tasks/:index/done` - mark the specified task as completed
- `DELETE /tasks/:index` - remove a task
- `POST /tasks/:index/pomodoro?work=25&rest=5` - start a Pomodoro timer for the task

Tasks are stored in `tasks.json` in the project root.
