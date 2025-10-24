// todo.js

export class TodoList {
  constructor() {
    this.tasks = [];
  }

  // Add a new task
  addTask(task) {
    this.tasks.push({ task, completed: false });
    console.log(`Task added: "${task}"`);
  }

  // Mark a task as complete (by task name)
  completeTask(taskName) {
    const task = this.tasks.find(t => t.task === taskName);
    if (task) {
      task.completed = true;
      console.log(`Task completed: "${taskName}"`);
    } else {
      console.log(`Task not found: "${taskName}"`);
    }
  }

  // List all tasks with status
  listTasks() {
    console.log('--- Todo List ---');
    this.tasks.forEach((t, i) => {
      console.log(`${i + 1}. ${t.task} [${t.completed ? 'Completed' : 'Pending'}]`);
    });
  }
}
