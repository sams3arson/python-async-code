def init_gen(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaException(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except BlaBlaException:
            break
        else:
            print("Message:", message)
    return "Returned from subgen()"

@init_gen
def delegator(g):
    #while True:
    #    try:
    #        message = yield
    #        g.send(message)
    #    except BlaBlaException as e:
    #        g.throw(e)
    try:
        print("I'm here!")
        result = yield from g
        print("And now here!")
    except StopIteration:
        print("Done!")
    finally:
        print(result)


sg = subgen()
dg = delegator(sg)

