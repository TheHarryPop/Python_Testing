from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def display_points(self):
        self.client.get('/displayBoard')

    @task
    def show_summary(self):
        self.client.post('/showSummary', {'email': 'kate@shelifts.co.uk'})

    @task
    def book(self):
        self.client.get('/book/Spring Festival/She Lifts')

    @task
    def purchase(self):
        self.client.post('/purchasePlaces', {'club': 'She Lifts', 'competition': 'Spring Festival', 'places': '4'})

    @task
    def logout(self):
        self.client.get('/logout')
