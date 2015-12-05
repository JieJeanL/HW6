class Expression:
    def __init__(self, expStr):
        expStr = "".join(expStr.split()) #whitespace strip
        while True:
            if expStr[0] == '-' or expStr[0] == '+':
                expStr = '0' + expStr
            print expStr
            try:
                num = float(expStr)
                self.left = None
                self.right = None
                self.op = None
                self.expStr = expStr
                return
            except:
                depth = 0
                op = -1
                opdex = None
                for i in range(len(expStr)):
                    char = expStr[i]
                    if char == '(':
                        depth += 1
                    elif char == ')':
                        depth -= 1
                    elif depth == 0 and char in '/*-+':
                        chardex = '/*-+'.index(char)
                        if chardex > op:
                            op = chardex
                            opdex = i
                if opdex is not None:
                    try:
                        self.op = '/*-+'[op]
                        self.left = Expression(expStr[:opdex])
                        self.right = Expression(expStr[opdex + 1:])
                        self.expStr = expStr
                        return
                    except:
                        raise ValueError
                elif len(expStr) > 1:
                    expStr = expStr[1:-1]
                else:
                    raise ValueError


    def evaluate(self):
        if self.op is None:
            return float(self.expStr)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.op == '*':
            return left * right
        elif self.op == '/':
            return left / right
        elif self.op == '-':
            return left - right
        elif self.op == '+':
            return left + right
        else:
            raise ValueError

    def printexpr(self):
        if self.op is None:
            return self.expStr
        else:
            return '(' + self.left.printexpr() + self.op + self.right.printexpr() + ')'

userinput = ''
while userinput != '#':
    try:
        userinput = raw_input("input an expression: ")
        myexp = Expression(userinput)
        #myexp = Expression('((5+5-2.5)*6/2-3)*3')
        #print myexp.left.expStr, myexp.op, myexp.right.expStr
        print 'your expression:', myexp.printexpr()
        print 'answer:', myexp.evaluate()
        print 'eval:', eval(userinput)
    except ValueError:
        print "malformed expression"
