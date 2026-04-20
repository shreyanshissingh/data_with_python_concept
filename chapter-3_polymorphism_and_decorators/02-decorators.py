def my_decorator(fx):
    def main_func(*args):
        print("Before Decorator -- adding a logic")
        response = fx(*args)
        print(response)
        print("After Decorator -- ending of logic")
        return response
    return main_func

@my_decorator
def fetch_data(url:str,path:str):
    # print(f"Fetching data from {url}, saving to path {path}")
    return f"Fetching data from {url}, saving to path {path}"

response = fetch_data("url.com","files/op")
print(response)