
def story(**kwds):
    return 'Once upon a time , there was a '\
            '{job} called {name}'.format_map(kwds)

def power(x,y,*others):
    if others:
        print('Received redundant parameters:',others)
    return power(x,y)

def interval(start,stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start,stop = 0,start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result