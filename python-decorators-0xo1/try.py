# # def add_one(number):
# #     return number + 1
# # print(add_one(2)) # Output: 3


# def say_hello(name):
#     return f"Hello {name}!"
# # print(say_hello('bib'))  # Output: Hello!

# def be_awesome(name):
#     return f"Yo {name}, together we're the awesome!"
# # print(be_awesome("Alice"))  # Output: Yo Alice, together we're the awesome!

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# def f():
#     s = f"I am a function and I am called {f.__name__}"
#     print(s)
    
# print('before the f()')

# f()
# print('after the f()')



# def decorator(func):

#     def first_child():
#         print("I am the first child")
#         func()
#         print("Yes, Something is happening after the function call")
#  
    # def say_whee():
#         print("whee!")

# say_whee = decorator(say_whee)


# from datetime import datetime

def decorator(func):
    def wrapper():
        print("I am awake")
        func()
        print("Sorry, end the function, I am sleeping")
         
    return wrapper

@decorator
def say_whee():
    print("Whee!")
# say_whee()