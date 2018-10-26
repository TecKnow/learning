import uuidv4 from "uuid/v4";

const fakeDatabase = {
  todos: [
    {
      id: uuidv4(),
      text: "hey",
      completed: true
    },
    {
      id: uuidv4(),
      text: "ho",
      completed: true
    },
    {
      id: uuidv4(),
      text: "let’s go",
      completed: false
    }
  ]
};

const delay = ms => new Promise((resolve, reject) => setTimeout(resolve, ms));

export const fetchTodos = filter =>
  delay(500).then(() => {
    switch (filter) {
      case "all":
        return fakeDatabase.todos;
      case "active":
        return fakeDatabase.todos.filter(t => !t.completed);
      case "completed":
        return fakeDatabase.todos.filter(t => t.completed);
      default:
        throw new Error(`Unknown filter: ${filter}`);
    }
  });
