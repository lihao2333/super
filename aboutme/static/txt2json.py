import sys,json,re,os
from anytree import Node, RenderTree
file_from, file_to = sys.argv[1], sys.argv[2]
def countPreSpace(string):#统计前面有几个空格
    _ = re.match(r"( *).*",string)
    if _:
        return len(_.group(1))
    else :
        return 0
last_parent = {}
for line in open(file_from).readlines():#构建anytree
    cntSpace = countPreSpace(line)
    name = line.strip()
    node = Node(name)
    last_parent[cntSpace] = node
    if cntSpace:
        node.parent = last_parent[cntSpace-4]
print(last_parent)    
for pre, fill, node in RenderTree(last_parent[0]):
    print("%s%s" % (pre, node.name))
def extractNode(node):#构建json
    d = {"name":os.path.basename(node.name)}
    res = []
    for cnode in node.children:
        res.append(extractNode(cnode))
    if res:
        d['children'] = res
    return d
resJson = extractNode(last_parent[0])
with open(file_to,"w") as f_to:
    f_to.write(json.dumps(resJson,ensure_ascii=False))
