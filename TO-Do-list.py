import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, master, text, command=None):
        self.var = tk.BooleanVar()
        self.frame = tk.Frame(master)
        self.checkbox = tk.Checkbutton(self.frame, text=text, variable=self.var, onvalue=True, offvalue=False)
        self.checkbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.frame.pack(fill=tk.X, pady=2)
        self.text = text

    def destroy(self):
        self.frame.destroy()

    def is_checked(self):
        return self.var.get()


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP To-Do List")
        self.tasks = []
        self.deleted_stack = []

        # Input Frame
        self.input_frame = tk.Frame(root)
        self.task_entry = tk.Entry(self.input_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        self.input_frame.pack(pady=10)

        # Task Frame
        self.task_frame = tk.Frame(root)
        self.task_frame.pack()

        # Control Buttons
        self.control_frame = tk.Frame(root)
        tk.Button(self.control_frame, text="Delete Selected", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Undo Delete", command=self.undo_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.control_frame, text="Clear All", command=self.clear_tasks).pack(side=tk.LEFT, padx=5)
        self.control_frame.pack(pady=10)

    def add_task(self):
        text = self.task_entry.get().strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return
        task = Task(self.task_frame, text)
        self.tasks.append(task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        any_deleted = False
        for task in self.tasks[:]:
            if task.is_checked():
                self.deleted_stack.append((task.text,))
                task.destroy()
                self.tasks.remove(task)
                any_deleted = True
        if not any_deleted:
            messagebox.showinfo("Delete Task", "No task selected for deletion.")

    def undo_task(self):
        if self.deleted_stack:
            text, = self.deleted_stack.pop()
            task = Task(self.task_frame, text)
            self.tasks.append(task)
        else:
            messagebox.showinfo("Undo", "No task to undo.")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            for task in self.tasks:
                task.destroy()
            self.tasks.clear()
            self.deleted_stack.clear()
            messagebox.showinfo("Cleared", "All tasks cleared.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
