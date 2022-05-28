# Team-A2
# Team-A2-Project

## **Index**

  1. Overview
  2. Installation
  3. Enviroment 
  4. Usage instructions
  5. Colaborators & contact inf0

## **Overview**

This python project is a tool to analyze measured a single or multiple .xlml data frames, with its output being a .png plot and a .xlmx file, according to customer demands.

## **Installation**

To install all the required modules just use the following command: 

```
pip install -r requierements.txt
```
## **Enviroment**

  - Windows10/11
  - Python 3.8

## **Usage instructions**

  1. Excute run.py
  2. Insert the desired wafers to analyze as shown in the example: 
  ```
  D07 D08
  ```
  In case o wanting to analyze all the wafers use command *All* instead: 
  ```
  All
  ```
  3. Insert the coordinates to analyze following the next format: 
  ```
  -4,-4/-4,3/0,1/1,-1
  ```
  Where the first term is the row the second the column number. To separate the coordinates simply use "/". In case of wanting to analyze all the possible coordinates just use the command *All*
  ```
  All
  ```
  4. Choose if you want to float the png files after executing the code. To accept just type: 
  ```
  y
  ```
  To deny type:
  ```
  n
  ```
  5. Choose if you want to save the plottings. To accept just type: 
  ```
  y
  ```
  To deny type:
  ```
  n
  ```
  6 Choose if you want to save an .xmlx file of the selected data. To accept just type: 
  ```
  y
  ```
  To deny type:
  ```
  n
  ```
  ## **Collaborators and contact info** 
  Seo Jinchan
  sjhmp21@hanyang.ac.kr
  
  Kim Chanyoung
  belljy@hanyang.ac.kr
  
  Jose Alan Barraza Villaverde
  al167694@alumnos.uacj.mx
