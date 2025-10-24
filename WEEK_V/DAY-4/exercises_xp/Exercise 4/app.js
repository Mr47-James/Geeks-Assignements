// app.js

import { TodoList } from './todo.js';

// Create an instance
const myTodo = new TodoList();

// Add some tasks
myTodo.addTask('Learn JavaScript');
myTodo.addTask('Write a blog post');
myTodo.addTask('Go for a walk');

// Complete a task
myTodo.completeTask('Write a blog post');

// List all tasks
myTodo.listTasks();
