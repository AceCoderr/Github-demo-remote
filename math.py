#add implementation
def add(x,y)
    return x+y
#subs implementation
def sub(x,y)
    return x-y  #on master
#multily implementation
def mul(x,y)
    return x*y  #on Bug456
#divide implementation
def div(x,y)
    if y==0:   #On master
        return DIVIDE_BY_0_ERROR
    else:
        return x/y


#sqaure implementation
def square(x):
    return x*x
