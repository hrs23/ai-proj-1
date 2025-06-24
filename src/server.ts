import express from 'express';
import fs from 'fs';
import path from 'path';

const app = express();
const PORT = process.env.PORT || 3000;
const TASKS_FILE = path.join(__dirname, '..', 'tasks.json');

app.use(express.json());

function loadTasks(): any[] {
  if (!fs.existsSync(TASKS_FILE)) {
    return [];
  }
  const data = fs.readFileSync(TASKS_FILE, 'utf-8');
  return JSON.parse(data);
}

function saveTasks(tasks: any[]) {
  fs.writeFileSync(TASKS_FILE, JSON.stringify(tasks, null, 2));
}

app.get('/tasks', (req, res) => {
  res.json(loadTasks());
});

app.post('/tasks', (req, res) => {
  const { description } = req.body;
  if (!description) {
    return res.status(400).json({ error: 'Description required' });
  }
  const tasks = loadTasks();
  tasks.push({ description, completed: false });
  saveTasks(tasks);
  res.json({ message: 'Task added', tasks });
});

app.put('/tasks/:index/done', (req, res) => {
  const idx = parseInt(req.params.index, 10) - 1;
  const tasks = loadTasks();
  if (idx < 0 || idx >= tasks.length) {
    return res.status(400).json({ error: 'Invalid task number' });
  }
  tasks[idx].completed = true;
  saveTasks(tasks);
  res.json({ message: 'Task completed', task: tasks[idx] });
});

app.delete('/tasks/:index', (req, res) => {
  const idx = parseInt(req.params.index, 10) - 1;
  const tasks = loadTasks();
  if (idx < 0 || idx >= tasks.length) {
    return res.status(400).json({ error: 'Invalid task number' });
  }
  const removed = tasks.splice(idx, 1)[0];
  saveTasks(tasks);
  res.json({ message: 'Task removed', task: removed });
});

app.post('/tasks/:index/pomodoro', (req, res) => {
  const idx = parseInt(req.params.index, 10) - 1;
  const work = parseInt(req.query.work as string) || 25;
  const rest = parseInt(req.query.rest as string) || 5;
  const tasks = loadTasks();
  if (idx < 0 || idx >= tasks.length) {
    return res.status(400).json({ error: 'Invalid task number' });
  }
  res.json({ message: `Pomodoro started for \"${tasks[idx].description}\"` });
  setTimeout(() => {
    console.log('Work period complete! Starting break.');
  }, work * 60000);
  setTimeout(() => {
    console.log('Break over! Good job!');
  }, (work + rest) * 60000);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
