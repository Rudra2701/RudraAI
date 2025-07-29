import Neuron
from Neuron import makearr


class Layer:
    def __init__(self,inputs,outputs):
        self.outputs=outputs
        x=makearr(inputs,-1,1)
        self.weights=[]
        for i in range(outputs):
            self.weights.append(x)
        self.bias=makearr(outputs,0,0)
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
"""
   Copyright 2025 Rudra Sahil Shivhare

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""