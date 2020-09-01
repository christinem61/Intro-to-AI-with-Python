# Traffic

An AI that uses Tensor Flow to build a neural network to classify road signs based
on an image of those signs.

What gave me the most accurate model was including 2 convolutional layers along with
2 pooling layers. The kernel size for both 2D convolutional layers were the same, but
the number of filters differed. I also included 2 hidden layers which used the ReLU function.
When I only had one hidden layer, the accuracy was a bit less accurate, so I decided to
stick with 2. Softmax activation was used for the output layer. 
Adding the dropout increased the accuracy of the model.

Video: https://youtu.be/PTnGe6ujr-Y
