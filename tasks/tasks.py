from locust import SequentialTaskSet, between, task


class MyTask(SequentialTaskSet):
    wait_time=between(1,5)

    @task
    def first_task(self):        
        with self.client.get('/api/users/2', catch_response=True) as response:
            if response.status_code != 200:
                response.failure('unable to navigate /api/users/2')
                            
    @task
    def second_task(self):        
        with self.client.get('/api/users/23', catch_response=True) as response:
            if response.status_code == 404:
                response.success()                
            else:
                response.failure('unable to navigate /api/users/2')
        
    @task
    def stop_task(self):
        self.interrupt()