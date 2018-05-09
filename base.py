__author__ = 'huke'

class input_buf():
    def __init__(self,data):
        self.data=data
        self.offset=0
    def str_pick(self):
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]
    def str_mv(self):
        self.offset += 1

class token():
    def consume(self,buff):
        pass

class data_token(token):
    def consume(self,data_buf):
        data_list=""
        while True:
            ch = data_buf.str_pick()
            if ch is None or ch not in "0123456789":
                break
            else:
                data_list +=ch
                data_buf.str_mv()
        if data_list != "":
            return ("int",int(data_list))
        else:
            return None

class op_token(token):
    def consume(self,data_buf):
        ch = data_buf.str_pick()
        if ch in "+-":
            data_buf.str_mv()
            return("op",ch)
        return None

def token_process(in_str):
    buf=input_buf(in_str)
    da_tk = data_token()
    op_tk = op_token()
    tokens=[]
    while buf.str_pick():
        token = None
        for tk in (da_tk,op_tk):
            token = tk.consume(buf)
            if token:
                tokens.append(token)
                break
    return tokens

# 表达式二叉树的节点
class Node(object):
    pass

class intNode(Node):
    def __init__(self,data):
        self.value=data


class opNode(Node):
    def __init__(self,data):
        self.op=data
        self.left=None
        self.right=None


def parser_token(token):
    lnode = intNode(token[0][1])
    tmp=None
    #last=token[0][0]
    for tok in token[1:]:
        last=tok[0]
        if tok[0]== 'op':
            tmp = opNode(tok[1])
            tmp.left=lnode
        if tok[0] == 'int':
            tmp.right=intNode(tok[1])
            lnode=tmp
    return lnode
'''
def tree_trave(parentNode):
    if parentNode == None:
        return
    tree_trave(parentNode.left)
    print(parentNode.value)
    tree_trave(parentNode.right)
'''

def calc(pnode):
    if isinstance(pnode.left,opNode):
        leftval=calc(pnode.left)
    else:
        leftval=pnode.left.value

    if pnode.op == '-':
        return leftval - pnode.right.value
    elif pnode.op == '+':
        return leftval + pnode.right.value


if __name__ == "__main__":
    prin_str=token_process("1+2-1")
    pnode=parser_token(prin_str)
    #print(pnode.op,pnode.left.op)
    #tree_trave(pnode)
    print(calc(pnode))

