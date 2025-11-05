def say_hello():
   name = input('What is your name? ')
   return 'Hello ' + name

def uppercase_decorator(func):
   def wrapper():
       original_func = func()
       modified_func = original_func.upper()
       return modified_func
   return wrapper

say_hello_res = uppercase_decorator(say_hello)

print(say_hello_res())