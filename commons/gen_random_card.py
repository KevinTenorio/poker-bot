import random

def gen_random_card():
    return f'{random.choice("23456789TJQKA")}{random.choice("cdhs")}'