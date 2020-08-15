<h1 align="center">Extensive Vision AI (EVA5)</h1>

<h2 align="center">Assignment- Architectural Basics</h2>

<h3 align="center"> Team Members: Prasad, Dheeraj, Rajesh, Vidhya Shankar </h3>

---
**Convolutions Architecture that achieves 99.4% accuracy for Mnist dataset**
---



**APPROACH AND SOLUTION**
----
The solution to identifying the right architecture that achieves the accuracy of 99.4% with less than 20K parameters and in 20 epochs is performed iteratively. A total of 6 different architectures were built iteratively and the summary of the trails are listed below. Refer to the link for the code.

**Summary of the trials**

1. Name: Original Architecture

   Description: Base architecture as provided by EVA, removed relu at conv7

   Parameters: 6.37 million

   number of Epochs - 1

   Accuracy - 98.7%

------------

2. Name: Trimming Parameters

  Description: Reduced the number of parameters by reducing channel size

  Parameters: 20930

  number of Epochs - 20

  Accuracy - 80.48%
  
------------

3. Name: Adding Gap

  Description : Add GAP to 5x5

  parameters = 9122

  number of epochs -20

  accuracy - 98.81 % -

--------------

4. Name: Batch Normalization

  Description : Batch Normalization

  parameters = 9170

  number of epochs -20

  accuracy - 98.04 % 
  
---------------------

5. Name: Architecture Optimization

  Description : Add parameters, Add 1*1 blocks

  parameters = 8.5K

  number of epochs -20

  accuracy - 99.46 % -


--------------------------


**Code Link**

colab - https://colab.research.google.com/drive/1NWCNq5Ze0ZLkAenFJPgqv7VEbFifFF95?usp=sharing

github - https://github.com/persie2212/Extensive_Vision_AI/blob/master/04.Architectural%20Basics/05_Architecture_Optimization.ipynb

-------------------

**ASK OF THE ASSIGNMENT**


1.  We have considered many many points in our last 4 lectures. Some of these we have covered directly and some indirectly. They are:
    1.  How many layers,
    2.  MaxPooling,
    3.  1x1 Convolutions,
    4.  3x3 Convolutions,
    5.  Receptive Field,
    6.  SoftMax,
    7.  Learning Rate,
    8.  Kernels and how do we decide the number of kernels?
    9.  Batch Normalization,
    10.  Image Normalization,
    11.  Position of MaxPooling,
    12.  Concept of Transition Layers,
    13.  Position of Transition Layer,
    14.  DropOut
    15.  When do we introduce DropOut, or when do we know we have some overfitting
    16.  The distance of MaxPooling from Prediction,
    17.  The distance of Batch Normalization from Prediction,
    18.  When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)
    19.  How do we know our network is not going well, comparatively, very early
    20.  Batch Size, and effects of batch size
    21.  etc (you can add more if we missed it here)
2.  Refer to this code:  [COLABLINK (links to an external site)](https://colab.research.google.com/drive/1uJZvJdi5VprOQHROtJIHy0mnY2afjNlx)
    -  **WRITE IT AGAIN SUCH THAT IT ACHIEVES**  
        1.  99.4% validation accuracy
        2.  Less than 20k Parameters
        3.  You can use anything from above you want.
        4.  Less than 20 Epochs
        5.  No fully connected layer