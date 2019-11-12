import random

def generate_input():
    raw_data = '\n'.join([ str(random.randint(0,10)) + ' ' + str(random.randint(0,10)) for _ in range(1000)])
    open('input.txt', 'w').write(raw_data)
    return raw_data