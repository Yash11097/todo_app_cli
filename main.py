import logic

class TODO:
    def __init__(self):
        while True:
            print("Welcome to the todo app what would you like to do? A - to add a new task B - to tick off a task of the list C - to view tasks Q - to exit")
            like_to_do = input("Put in your letter here?\n").upper()
            if like_to_do == "A":
                self.add_task()
            elif like_to_do == "B":
                self.tick_task()
            elif like_to_do == "C":
                self.read_task()
            elif like_to_do == "Q":
                break
    def add_task(self):
        task = input("What would you like to add?\n")
        logic.object.write(task)
    def read_task(self):
        logic.object.read()
        for task, number in enumerate(logic.object.list_of_tasks):
            print(f"{number} - {task + 1}")
    def tick_task(self):
        for tasks, number in enumerate(logic.object.list_of_tasks):
            print(f"{number} - {tasks + 1}")
        task = int(input("Which number would you like to tick off?\n"))
        for number, job in enumerate(logic.object.list_of_tasks):
            if number == task - 1:
                logic.object.remove_task(job)
todo_object = TODO()


        

