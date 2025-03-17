import json
import os

class To_dolist:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.list = self.load_list()  

    def load_list(self):
        if os.path.exists(self.filename):  
            with open(self.filename, "r") as file:
                return json.load(file)
        return []  

    def save_list(self):
        with open(self.filename, "w") as file:
            json.dump(self.list, file, indent=4)

    def add_list(self, list):
        self.list.append({"task": list, "Completed": False})  
        self.save_list()
        print(f"Task '{list}' added successfully.")

    def view_list(self,):
        if not self.list:
            print("No task Avaliable.")
        else:
            for idx , task in enumerate(self.list, 1):
                if task["Completed"]:
                    status = "Completed"
                else:
                    status = "Not Completed"
                print(f"{idx}. {task['task']} [{status}]")

    def mark_completed(self, list_index):
        if 0 <= list_index < len(self.list):
            self.list[list_index]["Completed"] = True
            self.save_list()
            print(f"Task '{self.list[list_index]["task"]}' marked as completed.")
        else:
            print("Invaild task number.")

    def remove_list(self, list_index):
        if 0 <= list_index < len(self.list):
            removed_task = self.list.pop(list_index)
            self.save_list()
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invaild task number.")

def main():
    todo = To_dolist()

    while True:
        print("\n----- To-Do List Application -----")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = int(input("Enter Your Choice ==> "))

        if choice == 1:
            task = input("Enter task: ")
            todo.add_list(task)
        elif choice == 2:
            todo.view_list()
        elif choice == 3:
            todo.view_list()
            task_no = int(input("Enter task number to mark as completed : ")) -1
            todo.mark_completed(task_no)
        elif choice == 4:
            todo.view_list()
            task_no = int(input("Enter task number to remove : ")) -1
            todo.remove_list(task_no)
        elif choice == 5:
            print("Goodbye!!")
            break
        else:
            print("Invalid choice! Please select the correct option.")

if __name__ == "__main__":
    main()
