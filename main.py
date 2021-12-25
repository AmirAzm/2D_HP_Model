import matplotlib.pyplot as plt


class Node:
    def __init__(self, x, y, label, action, dir):
        self.x = x
        self.y = y
        self.label = label
        self.action = action
        self.dir = dir

    def printN(self):
        print('('+str(self.x)+','+str(self.y)+') , '+self.label+' , '+self.action+' , '+self.dir)
        return


def en_f( nodes,alpha):
    c = 0
    for i,node in enumerate(nodes):
        if node.label == 'H':
            node_p = nodes[i+3:]
            for j in node_p:
                if j.label == 'H':
                    if (abs(node.x - j.x) == 0 and abs(node.y - j.y) == 1) or (abs(node.x - j.x) == 1 and abs(node.y - j.y) == 0):
                        print((node.x, node.y), (j.x, j.y))
                        c = c+1
    return c *alpha
def HH_C(S,A):
    if len(S) - 1 == len(A):
        A = A + "*"
        nodes = []
        valid = True
        nodes.append(Node(0, 0, S[0], A[0], '+x'))
        S = S[1:]
        A = A[1:]
        last = [nodes[0].x, nodes[0].y, nodes[0].action, nodes[0].dir]
        for s, a in zip(S, A):
            x = last[0]
            y = last[1]
            l_A = last[2]
            l_dir = last[3]
            if l_A == 'L' and l_dir == '+x':
                y = y + 1
                l_dir = '+y'
            elif l_A == 'L' and l_dir == '-x':
                y = y - 1
                l_dir = '-y'
            elif l_A == 'L' and l_dir == '+y':
                x = x - 1
                l_dir = '-x'
            elif l_A == 'L' and l_dir == '-y':
                x = x + 1
                l_dir = '+x'
            elif l_A == 'F' and l_dir == '+x':
                x = x + 1
                l_dir = '+x'
            elif l_A == 'F' and l_dir == '-x':
                x = x - 1
                l_dir = '-x'
            elif l_A == 'F' and l_dir == '+y':
                y = y + 1
                l_dir = '+y'
            elif l_A == 'F' and l_dir == '-y':
                y = y - 1
                l_dir = '-y'
            elif l_A == 'R' and l_dir == '+x':
                y = y - 1
                l_dir = '-y'
            elif l_A == 'R' and l_dir == '-x':
                y = y + 1
                l_dir = '+y'
            elif l_A == 'R' and l_dir == '+y':
                x = x + 1
                l_dir = '+x'
            elif l_A == 'R' and l_dir == '-y':
                x = x - 1
                l_dir = '-x'
            if a == '*':
                l_dir = '*'
            for node in nodes:
                if (node.x, node.y) == (x, y):
                    valid = False
            nodes.append(Node(x, y, s, a, l_dir))
            last = [x, y, a, l_dir]
        if valid:
            print('********************* HH - NODES  **********************')
            en = en_f(nodes, -1)
            x_s = []
            y_s = []
            print("***************************** NODES ***********************")
            for node in nodes:
                node.printN()
                x_s.append(node.x)
                y_s.append(node.y)
                if node.label == 'H':
                    plt.scatter(node.x, node.y, color='red', s=200, zorder=2)
                else:
                    plt.scatter(node.x, node.y, color='blue', s=200, zorder=2)
            plt.plot(x_s, y_s, color='black', zorder=1, lw=5)
            plt.gca().set_aspect('equal')
            plt.title("Energy = "+str(en))
            plt.show()
        else:
            print('There are nodes that are overlap')
    else:
        print("Sequence is Not VALID")


S = input('Enter HP sequence (H,P) :')
A = input('Enter direction sequence(F,R,L)('+str(len(S)-1)+' characters) :')
HH_C(S, A)

