from collections import *
w_list=["dog","cat","dog","dog","dog","cat"]
w_list.append("cat")
cou = Counter(w_list)
print("dof = ",cou.get("dog"))
print("cat=",cou.get("cat"))
