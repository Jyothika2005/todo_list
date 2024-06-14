import tkinter as tk
from tkinter import messagebox

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("400x400")

        # List to store tasks
        self.tasks = []

        # Input frame
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, width=30, font=('arial', 14))
        self.task_entry.pack(side=tk.LEFT, padx=10)

        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT)

        # Task list frame
        self.task_frame = tk.Frame(self)
        self.task_frame.pack(pady=20)

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self, task):
        self.tasks.remove(task)
        self.update_task_list()

    def update_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in self.tasks:
            task_frame = tk.Frame(self.task_frame)
            task_frame.pack(fill=tk.X, pady=2)

            task_label = tk.Label(task_frame, text=task, font=('arial', 14))
            task_label.pack(side=tk.LEFT, padx=10)

            remove_button = tk.Button(task_frame, text="Remove", command=lambda task=task: self.remove_task(task))
            remove_button.pack(side=tk.RIGHT)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
