import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("To-Do List")
window.geometry("350x550")
window.configure(bg="light green")



def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks.curselection()
    if selected_task_index:
        tasks.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    tasks.delete(0, tk.END)

lbl1=tk.Label(window, text= "TO-DO LIST", font="normal 15 bold",fg="black",bd=5).pack(side="top",pady=20)

entry = tk.Entry(window, font="normal 20 bold",width=20)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task",font="normal 10 bold",width=15, command=add_task)
add_button.pack()

remove_button = tk.Button(window, text="Remove Task",font="normal 10 bold",width=15, command=remove_task)
remove_button.pack()

clear_button = tk.Button(window, text="Clear All Tasks",font="normal 10 bold",width=15, command=clear_tasks)
clear_button.pack()

tasks = tk.Listbox(window,font="normal 13 bold", width=30)
tasks.pack(pady=10)

exit_button = tk.Button(window, text="Exit",font="normal 10 bold",width=15, command=window.destroy)
exit_button.place(x=110,y=450)

lbl=tk.Label(window, text= "Made By Ojasv Chaudhary", font="normal 11 bold",fg="black",bg="light green").place(x=90,y=500)

window.mainloop()
