from locust import between,HttpUser
from tasks.new_tasks import MyNewTask

from tasks.tasks import MyTask

class MyUser(HttpUser):    
    tasks = [MyTask,MyNewTask]