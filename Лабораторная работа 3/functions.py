import random

def get_list():
    our_number = str(random.randint(10**20, 10**30))
    our_list = [int(x) for x in our_number]
    return our_list