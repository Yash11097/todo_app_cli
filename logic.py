import json
class Logic:
    def __init__(self):
        self.all_data = []
        self.list_of_tasks = []


    def write(self, todo):

        data = todo
        self.all_data.append(data)
        with open("data.json", "w") as file:
            json.dump(self.all_data, file)
    def read(self):

        with open("data.json", "r") as file:
            data = json.load(file)
        self.list_of_tasks = data
    def remove_task(self, task):
        with open("data.json", "r") as file:
            data = json.load(file)
        for item in data:
            if task == item:
                self.list_of_tasks.remove(task)
                with open("data.json", "w") as file:
                    json.dump(self.list_of_tasks, file)
object = Logic()

