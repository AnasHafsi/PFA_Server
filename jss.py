import json
import numpy as np
s = "{'block':[{'col':2,'f':0,'g':0,'h':0,'parent':null,'row':1,'block':false},{'col':1,'f':0,'g':0,'h':0,'parent':null,'row':2,'block':false},{'col':2,'f':0,'g':0,'h':0,'parent':null,'row':2,'block':false},{'col':3,'f':0,'g':0,'h':0,'parent':null,'row':3,'block':false}],'columns':5,'d':{'col':1,'f':0,'g':0,'h':0,'parent':null,'row':1,'block':false},'f':{'col':4,'f':0,'g':0,'h':0,'parent':null,'row':4,'block':false},'path':null,'rows':5}"
s = s.replace("\'", "\"")
obj = json.loads(s)


dim = (obj["columns"], obj["rows"])
maze = np.zeros(dim,dtype=int)
start = (obj["d"]["col"], obj["d"]["row"])
fin = (obj["f"]["col"], obj["f"]["row"])
blo  = (obj["block"][0]["col"])
print(len(obj["block"]))

for i in range(len(obj["block"])):
    maze[obj["block"][i]["col"]][obj["block"][i]["row"]]=1
print(start,fin,blo)
print(maze)
