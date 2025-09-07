def simple_generator():
    for i in range(5):
        yield i

for num in simple_generator():
    print(num)
