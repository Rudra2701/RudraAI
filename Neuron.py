def multiply(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c

def neuron(inputs,weights,bias=0):
    return sum(multiply(inputs,weights))+bias
