#Aim:implementing AND,NOT and OR gate using McCulloch pitts neuron model
#Name:jeet Shah
#roll number:E024
#Batch: B.Tech CSE BE1

if __name__ == "__main__":
    w1=1#weights of each node
    w2=1
    x1=int(input("please enter the input1:"))#entered the weight values
    x2=int(input("please enter the input2:"))
    
    #implementing individual gates for the respective nodes
    #FOR OR GATE
    outputOr=0
    thresholdOr=1#calculated threshold with respect to the desired output
    inputOr=(x1*w1)+(x2*w2)
    if(inputOr>=thresholdOr):
        outputOr=1
    print('the output value for the OR neuron is ',outputOr)
    
    #FOR AND GATE
    outputAnd=0
    thresholdAnd=2#calculated threshold with respect to the desired truth table
    inputAnd=(x1*w1)+(x2*w2)
    if(inputAnd>=thresholdAnd):
        outputAnd=1
    print('the output value of the AND neuron is ',outputAnd)
    
    #FOR NOT GATE
    outputNot1=0
    outputNot2=0
    thresholdNot=1
    inputNot1=x1*w1
    inputNot2=x2*w2
    if(inputNot1<thresholdNot):
        outputNot1=1
    if(inputNot2<thresholdNot):
        outputNot2=1
    print('the output for first node with not is ',outputNot1)
    print('the output for second node with not is ',outputNot2)