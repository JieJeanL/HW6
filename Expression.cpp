/*
 * Name: Ian Prins, Jie Luo, Eric Chaput, Jiamin Luo
 * MacID: prinsij, luoj3, chaputem, luoj1
 * Student Number: 001419316, 001416119, 
 * Description: This file implements the class Add, representing an addition 
 * 				arithmatic expression
 */
#include <iostream>
#include <string>
#include <stdio.h>
#include "Expression.h"
using namespace std;

class Expression{
  //evaluate expression and return string representation of the result
  virtual string evaluate();
  
  //prints expression
  virtual void print();
  
}
