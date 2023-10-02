class Node:
    def __init__(self,char,freq,left=None,right=None) -> None:
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.char}"

    def __lt__(self, other: 'Node'): # a < b
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            mytemp = ord(self.char) if self.char != '*' else -1
            othertemp = ord(other.char) if other.char != '*' else -1
            return mytemp < othertemp
        else:
            return False

def printTree(node: Node , level = 0):        
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def encode(node:Node,new_dict,path=""):
    if node != None:
        encode(node.right, new_dict, path+"1")
        if node.char != "*":
            new_dict[node.char] = path
        encode(node.left, new_dict,path+"0")


def encodeToBi(string,dic):
    encode_msg = ""
    for ch in string:
        encode_msg+=dic[ch]
    return encode_msg

def getHeight(node:Node):
    if node == None:
        return 0
    return max(getHeight(node.left) ,getHeight(node.right))+1


message = input("Enter Input : ")
char_freq = {}
for ch in message:
    if ch not in char_freq:
        char_freq[ch] = 1
    else:
        char_freq[ch] += 1
node_list = [Node(ch,freq) for ch,freq in char_freq.items()]
node_list.sort(reverse=True)

while len(node_list) > 1:
    temp1 = node_list.pop()
    temp2 = node_list.pop()
    node_list.insert(0,Node("*",temp1.freq+temp2.freq,temp1,temp2))
    node_list.sort(reverse=True)
encodeDict = {}
encode(node_list[0],encodeDict)
print(encodeDict)
printTree(node_list[0])
print(f"Encoded! : {encodeToBi(message,encodeDict)}")


