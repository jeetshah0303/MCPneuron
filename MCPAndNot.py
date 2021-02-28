#Implementing ANDNOT gate using McCulloch Pitts neuron model
w1=1#weights of each node
w2=-1
x1=int(input("please enter the input1:"))#entered the weight values
x2=int(input("please enter the input2:"))
thresh2=1
outputLayer2=0
inputLayer2=(x1*w1)+(x2*w2)
if(inputLayer2>=thresh2):
        outputLayer2=1
print('the output of ANDNOT is ',outputLayer2)