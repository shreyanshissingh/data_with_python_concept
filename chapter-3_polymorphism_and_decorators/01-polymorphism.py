class fetch_from_api:
    
    def fetch(self):
        print(f"Fetch from API")
class fetch_from_db:
    def fetch(self):
        print(f"Fetch from DB")
class fetch_from_other:
    def fetch(self):
        print(f"Fetch from Other Source")

obj = fetch_from_db()
obj.fetch()