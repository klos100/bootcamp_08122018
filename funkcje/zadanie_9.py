import time

start = time.time()
lista = [x*2 for x in range(1000000)]
stop = time.time()
print(stop-start)



def log(funkcja):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = funkcja(*args,**kwargs)
        stop = time.time()
        trwanie = stop-start
        print(f"Dlugosc wywolania {funkcja.__name__} to {trwanie}s")
        return result
    return wrapper

@log
def foo(arg):
    return f'To jest{arg}'
foo("1")


# def test_dekoracja_foo():
#     assert foo(1) == "Dlugosc wywolania foo to x"