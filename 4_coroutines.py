# coroutines are generators that receive values
# if you place `yield` after `=`, you can pass values to that generator

# на вызове next() сначала отдается значение после yield, а после него
# нужно использовать метод send(value) для отправки значения в генератор

def subgen():
    message = yield "ебать вот это шайтан машина"
    print("Subgen received:", message)

def init_gen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

@init_gen
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average

avg = average()
print(avg.send(5))
print(avg.send(10))
try:
    avg.throw(StopIteration)
except StopIteration as e:
    print("Average:", e.value)
