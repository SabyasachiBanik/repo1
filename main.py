def hailstone(n):
    #if type(n)!= int:
    if not isinstance(n, int):
        print("give an integer")
        return
    if n<=0:
        print("n should be positive")
        return

    l=[n]
    while n!=1:
        n = n // 2 if not n % 2 else 3 * n + 1
        l.append(n)
    return l

#print(hailstone(16))
class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
root = Node(10, Node(5, Node(3), Node(18)), Node(15, Node(8)))
def range_sum(node, lower, upper):
    s = 0
    if node.l is not None:
        s += range_sum(node.l, lower, upper)
    if node.r is not None:
        s += range_sum(node.r, lower, upper)
    if lower <= node.v < upper:
        s += node.v
    return s
print(range_sum(Node(2, Node(3, Node(4))), 2, 4))



