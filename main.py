from Day1ContainDup import SolutionContain as DupSol
from Day2ValidAnagram import SolutionDiagram as AnaSol
# TODO : DO THE ORD USING BIT AND BYTE
# TODO : PROPER CLASS METHODS  

# Question Variables 
Q_1 = [1,0,1,3,3,4,3,2,4,2]
print("--Solutions Day One If Contain Duplicate!--")
print("1. Does Contain Duplicate?  [1,1,1,3,3,4,3,2,4,2] \n Answer : {}\n Sorted: {}\n RunTime: {}".format(DupSol().duplicate(Q_1)[0], DupSol().duplicate(Q_1)[1], DupSol().duplicate(Q_1)[2]))

Q_2_s, Q_2_t = "anagram","nagaram"

print("2. Is this two \"{1}\", \"{2}\" string Valid Anagram?  \n Answer: {0}".format(AnaSol().Anagram(Q_2_s,Q_2_t),Q_2_s,Q_2_t))
