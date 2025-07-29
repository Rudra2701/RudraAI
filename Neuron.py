import random
def makearr(x,l,u):
    return [random.uniform(l,u) for i in range(x)]

def multiply(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c

def neuron(inputs,weights,bias=0):
    return max(sum(multiply(inputs,weights))+bias,0)
class Neuron:
    def __init__(self,inputs,l=-1,u=1,bias=0):
        #self.weights=weights
        self.bias=bias
        self.weights=makearr(inputs,l,u)
    def get(self,inputs):
        return neuron(inputs,self.weights,self.bias)
    def weights(self,x,weight):
        self.weights[x]=weight
    def bias(self,bias):
        self.bias=bias
    def get_weights(self):
        return self.weights
    def get_bias(self):
        return self.bias
    def change_weights(self,weights):
        for i in range(len(weights)):
            self.weights+=i
    def change_bias(self,bias):
        self.bias+=bias
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