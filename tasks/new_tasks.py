from locust import SequentialTaskSet, between, task
class MyNewTask(SequentialTaskSet):
    wait_time=between(1,5)

    @task
    def third_task(self):
        with self.client.get('/api/unknown/2', catch_response=True) as response:
            if(response.status_code != 200):
                response.failure("unable to fetch /api/unknown/2")            

    @task
    def fourth_task(self):
        with self.client.get('/api/unknown', catch_response=True) as response:
            if(response.status_code != 200):
                response.failure('unable to fetch /api/unkown')
    
    @task
    def stop_task(self):
        self.interrupt()