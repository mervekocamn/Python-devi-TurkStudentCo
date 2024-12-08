import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def addTask(self, taskName):
        newTask = Task(taskName)
        self.tasks.append(newTask)
        self.save_tasks()
        print("Görev eklendi.")

    def deleteTask(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
            print("Görev silindi.")
        else:
            print("Geçersiz görev numarası.")

    def getTask(self):
        if not self.tasks:
            print("Görev yok")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Tamamlandı" if task.completed else "Devam Ediyor"
                print(f"{idx + 1}. {task.name} - {status}")

    def changeState(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()
            print("Görev tamamlandı.")
        else:
            print("Geçersiz görev numarası.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.name},{task.completed}\n")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for line in file:
                    name, completed = line.strip().split(",")
                    self.tasks.append(Task(name, completed == "True"))


def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Görev Ekle")
        print("2. Tamamlandı olarak işaretle")
        print("3. Görev Sil")
        print("4. Tüm görevleri getir")
        print("5. Çıkış")

        choice = input("İşlem seçiniz: ")

        if choice == "1":
            task_name = input("Görev adı: ")
            task_manager.addTask(task_name)
        elif choice == "2":
            task_manager.getTask()
            task_index = int(input("Tamamlanmış görev numarasını seçiniz: ")) - 1
            task_manager.changeState(task_index)
        elif choice == "3":
            task_manager.getTask()
            task_index = int(input("Silmek istediğiniz görevin numarasını giriniz: ")) - 1
            task_manager.deleteTask(task_index)
        elif choice == "4":
            task_manager.getTask()
        elif choice == "5":
            print("Çıkış yapıldı")
            break
        else:
            print("Lütfen yukarıdaki seçeneklerden birini seçiniz")

main()
