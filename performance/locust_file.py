from locust import HttpUser, task, between

class ContactUser(HttpUser):
    wait_time = between(2, 5) # Increased to be more "human-like"

    def on_start(self):
        with self.client.post("/users/login", json={
            "email": "testuserdimple@example.com", 
            "password": "Password123"
        }, catch_response=True) as response:
            if response.status_code == 200:
                token = response.json().get("token")
                self.client.headers.update({"Authorization": f"Bearer {token}"})
            else:
                response.failure(f"Login failed: {response.status_code}")

    @task
    def load_contacts(self):
        # Stopping the task from running if the token was never grabbed
        if "Authorization" in self.client.headers:
            self.client.get("/contacts", name="Authenticated View Contacts")