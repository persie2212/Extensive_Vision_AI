<h1 align="center">Extensive Vision AI (EVA5)</h1>

<h2 align="center">Assignment- Receptive Fields & Network Architectures</h2>

<h3 align="center"> Team Members: Prasad, Dheeraj, Rajesh, Vidhya Shankar </h3>

---
**Resnet Architecture that achieves 85% accuracy for CIFAR10 dataset**
---



**APPROACH AND SOLUTION**
----
The solution to incorporate the resnet architecture that achieves the accuracy of more than 85% accuracy

Steps:
Added Resnet module from https://github.com/kuangliu/pytorch-cifar. Achieved 84% accuracy. 
Played around with transformation by changing Hue, contrast and brightness and learning rate. Reached 86% accuracy. 


**Summary of the trials**

1. Name: Resnet Architecture

![alt text](https://github.com/persie2212/Extensive_Vision_AI/blob/master/08.Receptive%20Fields%20%26%20Network%20Architectures/Images/Architecture-of-ResNet-18.png)


   Description: Added Resnet-18 Archtecture
   Parameters: 11,173,962

   number of Epochs - 20

   Accuracy - 86.54%



**Code Link**

colab - https://colab.research.google.com/drive/15Yqmey9PzMehxAF93R0COZEvCNxNIJDj#scrollTo=zbpEilw-vNCY

github - https://github.com/persie2212/Extensive_Vision_AI/tree/master/08.Receptive%20Fields%20%26%20Network%20Architectures

-------------------

**ASK OF THE ASSIGNMENT**    

1.  Refer to this code:  [COLABLINK (links to an external site)](https://colab.research.google.com/drive/1uJZvJdi5VprOQHROtJIHy0mnY2afjNlx)
    -  **WRITE IT AGAIN SUCH THAT IT ACHIEVES**  
    1.  change the code such that it uses GPU
	2.	change the architecture to C1C2C3C40 (basically 3 MPs)
	3.	total RF must be more than 44
	4.	one of the layers must use Depthwise Separable Convolution
	5.	one of the layers must use Dilated Convolution
	6.	use GAP (compulsory):- add FC after GAP to target #of classes (optional) achieve 80% accuracy, as many epochs as you want. Total Params to be less than 1M. 
