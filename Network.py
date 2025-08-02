from Layer import *
class Network:
    def __init__(self,input_size,hidden_size,output_size,upper=1,lower=-1):
        self.hidden=Layer(input_size,hidden_size,lower,upper)
        self.output=Layer(hidden_size,output_size,lower,upper)
        self.inputs=input_size
        self.hiddens=hidden_size
        self.outputs=output_size
    def get(self,inputs):
        return self.output.feedforward(self.hidden.feedforward(inputs))
    def get_weights_hidden(self):
        o=[]
        for a in self.inputs:
            self.hidden.get_weights(a)
            o.append(self.hidden.get_weights(a))
        return o
    def get_weights_output(self):
        o=[]
        for a in self.hiddens:
            self.output.get_weights(a)
            o.append(self.output.get_weights(a))
    def get_bias_hidden(self):
        o=[]
        for a in self.hiddens:
            o.append(self.hidden.get_bias(a))
        return o
    def get_bias_output(self):
        o=[]
        for a in self.outputs:
            o.append(self.output.get_bias(a))
        return o
    def change_weights_hidden(self,weights):
        for i in range(len(weights)):
            self.hidden.change_weights(i,weights[i])
    def change_weights_output(self,weights):
        for i in range(len(weights)):
            self.output.change_weights(i,weights[i])
    def change_bias_hidden(self,bias):
        for i in range(len(bias)):
            self.hidden.change_bias(bias[i])
    def change_bias_output(self,bias):
        for i in range(len(bias)):
            self.output.change_bias(bias[i])
