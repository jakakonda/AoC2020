import operator


IN = 'input.txt'
with open(IN, 'r') as f:
    exprs = [line.replace(')', ' ) ').replace('(', ' ( ').strip().split() for line in f]


# Part 1
class ExprBuilder:
    def __init__(self, expr):
        self.expr = expr
        self.pos = 0

    def parse(self, is_right=False):
        while self.pos < len(self.expr):
            c = self.expr[self.pos]
            self.pos += 1

            if c == '(':
                expr = (True, self.parse()) # Mark nested
            elif c == ')':
                return expr 
            elif c.isnumeric():
                expr = (False, int(c))
            else: # operator
                expr = (False, c, expr, self.parse(is_right=True))
            
            if is_right:
                break

        return expr


def calc(expr):
    # Nested expr
    if expr[0] == True:
        return calc(expr[1])
    # Number
    if type(expr[1]) == int:
        return expr[1]

    ops = {
        '+': operator.add,
        '*': operator.mul
    }
    
    l = calc(expr[2])
    r = calc(expr[3])
    return ops[expr[1]](l, r)


total = 0
for i in exprs:
    expr = ExprBuilder(i).parse()
    total += calc(expr)

print(total)


# Part 2
# Inside the expression, sunk the + operators to the bottom
def rebalance(expr):
    # Expr
    if expr[0] == True:
        return (True, rebalance(expr[1])) # Rebalance as standalone expression
    # Number
    if expr[0] == False and type(expr[1]) == int:
        return expr # Nothing to do with numbers
    
    # Operator
    l = rebalance(expr[2])
    r = rebalance(expr[3])

    # Sunk
    # Swap operators
    # Parent is new right
    # Left is new parent
    # Left (Right) is new left
    if l[0] == False and l[1] == '*' and expr[1] == '+':
        expr = (False, '+', l[3], r)
        l = (False, '*', l[2], expr)
        return l
    else:
        return (expr[0], expr[1], l, r)


total = 0
for i in exprs:
    expr = ExprBuilder(i).parse()
    expr = rebalance(expr)
    total += calc(expr)

print(total)
