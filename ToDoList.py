##TODO list application
class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def ad_task(self,task):
        self.tasks.append(task)

    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
    
    def get_all_tasks(self):
        return self.tasks

    def mark_task_completed(self,task):
        if task in self.tasks:
            index = self.tasks.index(task)
            self.tasks[index] = f"{task} - Completed"
# Example usage

todo = ToDoList()
todo.ad_task("Buy groceries")
todo.ad_task("Read a book")
print("All Tasks:", todo.get_all_tasks())
todo.mark_task_completed("Buy groceries")
print("All Tasks after marking one as completed:", todo.get_all_tasks())
todo.remove_task("Read a book")
print("All Tasks after removing one:", todo.get_all_tasks())
