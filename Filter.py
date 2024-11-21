import matplotlib.pyplot as pl

def get_Variable(info, var):
    print(info[var])
#

def scatter(info, x, y):
    pl.scatter(info[x],info[y])
    pl.xlabel(x)
    pl.ylabel(y)
    pl.show()
    