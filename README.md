# pyqt6_calculator
I designed the calculator myself using pyqt6 and proceeded with the calculator project that followed the four arithmetic operation rule algorithm

## Introduction

### Title
| Name | make a simple calculator using pyqt6 |
|:---|:---|
| Background | Challenges for Instead of using convenient functions, I write code while designing the computational algorithm myself

### Tech Stack
|Part|Technologies|
|---|---|
|Development<br/>Environment|<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white"/> <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white"/>|
|Language|<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/> 
|Hardware|<img src="https://img.shields.io/badge/-PyQt-004400?style=flat&logo=Qt"/> 
|Collaborative Tools| <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/> |

## 0. Research Background

### Learning and Understanding Algorithms for Four Arithmetica Rules?

In fact, there is a function called eval() in Python that outputs strings at once by replacing them with integers and real numbers. However, instead of using the eval() function, I wanted to study computational algorithms by using a direct computational algorithm. While doing a lot of research, there is an algorithm called Reverse Polish Notation (RPN) Evaluation, which I use to implement a simple calculator myself

## 1. Conceptual Design

### 1-1. Feature list

| No. | Function | Description |
|:---:|---|---|
|UR_01| AC | AC is fully initialized |
|UR_02| C | C removes only the last one from the current number |
|UR_03| 0~9 | Screen output when inputting the button |
|UR_04| 0 |If it's 0 when you first enter it, make sure it doesn't press more than that|
|UR_05| Operator duplicate |When the operator comes in, move on|
|UR_06| Continuous computational function |=Additional expressions can be calculated by pressing the button|
|UR_07| point |decimal entry function|
|UR_08| The four fundamental arithmetic operations |=+,-,*,/' Calculate to prioritize|
|UR_09| Result |=Output result using button|

### 1-2. Calculator designed by pyqt6

![image](https://github.com/user-attachments/assets/99325b6e-bff3-4204-a978-fceef80c025b)


## 2. Detailed Design (Sequence diagram)

![calculator drawio](https://github.com/user-attachments/assets/aad01e7d-8415-4122-ba01-75917b6045ac)


## 3. Testing

![image](https://github.com/user-attachments/assets/1163b5f3-e8f3-451f-865f-ccfb55694f1e)

### 3-1. Calculating sequence

![image](https://github.com/user-attachments/assets/ee904761-4395-4213-b660-ffdd895430e0)

## 4. Testcase

| No. | Case | Check |
|:---:|---|---|
|tc_case|||
|TC_01| Is the number no longer pressed than when I first hit 0? | O |
|TC_02| Does a number change to a single digit when pressed in 0 state? | O |
|TC_03| Does dividing by 0 result in an error? | O |
|TC_04| Can decimal point be calculated? | O |
|TC_05| Did you prevent it from becoming an overplot operation? | O |
|TC_06| Did you follow the four-principle calculation rules? | O |
|TC_07| Does it distinguish operators from negative numbers exactly? | O |
|TC_08| Is the clear button running? | O |
|TC_09| Is the All Clear button running? | O |
|TC_10| Is it possible to perform additional operations in the formula in which the calculation results are coming out | O |
