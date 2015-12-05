/*
 * Name: Ian Prins, Jie Luo, Eric Chaput, Jiamin Luo
 * MacID: prinsij, louj3, chaputem, luoj1
 * Student Number: 001419316, 
 * Description: This file implements the class Add, representing an addition 
 * 				arithmatic expression
 */
 #include <iostream>
 #include <string>
 #include <stdio.h>
 #include "Expression.h"
 #include "ArithmeticExpression.h"
 using namespace std;
  
//string ArithmeticExpression::evaluate(){};
		
float ArithmeticExpression::convert(string s){
	return stof(s);
}

ArithmeticExpression ArithmeticExpression::constructArith(string s){
	for (int i=0; i < s.length(); i++){
		if (s[i] == ' '){
			s.erase(i, 1);
		}
	}
	while(true){
		if (s[0] == '-' || s[0] == '+'){
			s = "0" + s;
		}
		cout << s;
		int depth = 0;
		int op = -1;
		int operationIndex;
		for (int i=0; i < s.length(); i++){
			if (s[i] == '('){
				depth = depth + 1;
			} else if (s[i] == ')'){
				depth = depth -1;
			} else if (depth == 0){
				if ("/*-+".find(s[i]) != string::npos){
					if ("/*-+".find(s[i] > op){
						operationIndex = i;
						op = "/*-+".find(s[i]);
					}
				}
			}
		}
		if (op > -1){
			this.
	}	
}