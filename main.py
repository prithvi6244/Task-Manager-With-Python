#Universally Unique Identifiers
import uuid,time
class Task:
    def __init__(self,task):
        self.task=task
        self.created_time=f'{time.ctime()}'
        self.updated_time="NA"
        self.completed_time="NA"
        self.task_done=False
        self.id=f'{uuid.uuid4()}'

    def update_task(self,name):
        self.task=name
        self.updated_time=f'{time.ctime()}'
    def complete_task(self):
        self.task_done=True
        self.completed_time=f'{time.ctime()}'
cnt=0
tasks=[]
incompleted=[]
completed=[]
tasks.append("Null")
def show(task):
    print(f'ID -- {task.id}')
    print(f'Task -- {task.task}')
    print(f'Created Time -- {task.created_time}')
    print(f'Updated Time -- {task.updated_time}')
    print(f'Completed -- {task.task_done}')
    print(f'Completed Time -- {task.completed_time}')

while True:
    print("-------------------------")
    print("1. Add New Task\n"
          "2. Show All Task\n"
          "3. Show Incomplete Tasks\n"
          "4. Show Completed Tasks\n"
          "5. Update Task\n"
          "6. Mark a Task Completed\n")
    print("-------------------------")
    a=input("Enter Option: ")
    if(a=='1'):
        tmp=input("Enter New Task:")
        cnt+=1
        tasks.append(Task(tmp))
        print("Task Created Successfully.")
        incompleted.append(tasks[cnt])
    elif a=='2':
        if len(tasks)==1:
            print("No completed tasks")
        for task in tasks:
            if task != 'Null':
                show(task)
                print()

    elif a=='3':
        if len(incompleted)==0:
            print("All Tasks are Completed")
        else:
            for task in incompleted:
                show(task)
                print()
    elif a=='4':
        if len(completed)==0:
            print("No Task are completed.")
        else:
            print("Completed Tasks ")
            print()
            for completed_task in completed:
                show(completed_task)
                print()
    elif a=='5':
        if len(incompleted)==0:
            print("There are no task to update")
        else:
            tmp=0
            print("Select which Task to update")
            print()
            for i in range(0,len(incompleted)):
                tmp=i+1
                print()
                print(f'TasK NO {tmp}')
                show(incompleted[i])
            tmp1=input("Enter Task NO:")
            tmp2=int(tmp1)
            if tmp2==0:
                print("Invalid Task NO")
            elif tmp2>len(incompleted):
                print("Invalid Task NO")
            else:
                tmp1=input("Enter New Task: ")
                incompleted[tmp2-1].update_task(tmp1)
                print("Task Updated Successfully.")
    elif a=='6':
        if len(incompleted) ==0:
            print("There are No tasks that are pending")
        else:
            print("Select which Task to complete")

            for i in range(0,len(incompleted)):
                tmp=i+1
                print()
                print(f'TasK NO {tmp}')
                show(incompleted[i])
            tmp1=input("Input Task NO: ")
            tmp2=int(tmp1)
            if tmp2==0:
                print("Invalid Task NO")
            elif tmp2>len(incompleted):
                print("Invalid Task NO")
            else:
                incompleted[tmp2-1].complete_task()
                completed.append(incompleted[tmp2-1])
                incompleted.pop(tmp2-1)
                print("Task Completed")








