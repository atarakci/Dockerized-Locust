import hashlib

from locust import HttpLocust, TaskSet, task


class EventCollector(TaskSet):

    @task
    def webRequest(self):
        self.client.get("")


class WebsiteUser(HttpLocust):
    task_set = EventCollector
    min_wait = 5000
    max_wait = 9000
