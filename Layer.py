import Neuron
from Neuron import makearr


class Layer:
    def __init__(self,inputs,outputs,lower=-1,upper=1):
        self.outputs=outputs
        x=makearr(inputs,lower,upper)
        self.weights=[]

        for i in range(outputs):
            self.weights.append(x)
        self.bias=makearr(outputs,lower,upper)
    def feedforward(self,inputs):
        o=[]
        for i in range(self.outputs):
             o.append(Neuron.neuron(inputs,self.weights[i],self.bias[i]))
        return o
    def weight(self,w,weight):
        self.weights[w]=weight
    def bias(self,b,bias):
        self.bias[b]=bias
    def get_weights(self,w):
        return self.weights[w]
    def get_bias(self,b):
        return self.bias[b]
    def change_weights(self,w,weight):
        for i in range(len(weight)):
            self.weights[w][i]+=weight[i]
    def change_bias(self,bias):
        for i in range(len(bias)):
            self.bias[i]+=bias[i]
