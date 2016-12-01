import hashlib

from locust import HttpLocust, TaskSet, task


class EventCollector(TaskSet):
    token = ""

    def on_start(self):
        self.token = self.generateToken()

    @task
    def mobileRequest(self):
        self.client.headers['Authorization'] = self.token
        self.client.headers['Content-Type'] = "application/json"
        self.client.post("/e", data="{\"event\":\"e\",\"k1\":\"v1\",\"sid\":\"0123456789\",\"pid\":\"0123456789\"}")

    @task
    def webRequest(self):
        self.client.headers['Authorization'] = self.token
        self.client.get("/__gc.gif?p=event||order||k1||v1")

    def generateToken(self):
        apiKey = "zxcasd"
        apiSecret = "123abc"
        nonce = "xxxaaa"
        hash_object = hashlib.sha256(apiKey + apiSecret + nonce)
        hex_dig = hash_object.hexdigest()

        result = "key=%s,token=%s,nonce=%s" % (apiKey, hex_dig, nonce)

        return result


class WebsiteUser(HttpLocust):
    task_set = EventCollector
    min_wait = 5000
    max_wait = 9000
