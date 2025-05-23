#manly yield kivabe kaj kore eita jana
def my_generator():
    yield 1 
    yield 2
    yield 3

for x in my_generator():
    print(x)
