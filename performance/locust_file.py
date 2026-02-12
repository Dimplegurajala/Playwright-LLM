from locust import HttpUser, task, between

class ContactUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """ This runs ONCE when a virtual user starts. It logs in and gets a token. """
        response = self.client.post("/users/login", json={
            "email": "testuserdimple@example.com", 
            "password": "Password123"
        })
        if response.status_code == 200:
            # Attaching the token to all future requests for this user
            token = response.json().get("token")
            self.client.headers.update({"Authorization": f"Bearer {token}"})

    @task
    def load_contacts(self):
       
        self.client.get("/contacts", name="Authenticated View Contacts")