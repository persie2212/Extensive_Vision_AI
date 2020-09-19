<h1 align="center">Extensive Vision AI (EVA5)</h1>

<h2 align="center">Assignment- Advanced Convolutions</h2>

<h3 align="center"> Team Members: Prasad, Dheeraj, Rajesh, Vidhya Shankar </h3>

---
**Convolutions Architecture that achieves 84.09% accuracy for CIFAR10 dataset**
---



**APPROACH AND SOLUTION**
----
The solution to identifying the right architecture that achieves the accuracy of more than 80% with less than 1M parameters and in 20 epochs is performed iteratively. 

**Summary of the trials**

1. Name: Advanced Convolutions

   Description: Added Gap, Diluted covolution and deprthwise convolution

   Parameters: 604K

   number of Epochs - 20

   Accuracy - 84.09%



**Code Link**

colab - https://colab.research.google.com/drive/1OfOze56WU8MOn5pBvDZCYarJ7w83Q5Db#scrollTo=s05iFZ-6-ION

github - https://github.com/persie2212/Extensive_Vision_AI/blob/master/04.Architectural%20Basics/05_Architecture_Optimization.ipynb

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