import functools as f

price = [500, 1000, 300, 700, 2000]

def gst(price):

    return list(map(lambda x: x * 0.18, price))



def f_filter (price):

    return list(filter(lambda x: x > 500, price))

get_total = gst(price) + f_filter(price)

def total(get_total):

    return f.reduce(lambda x, y: x + y, get_total)

print (gst(price))
print (f_filter(price))
print (total(get_total))
