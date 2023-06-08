"""
    Valid Diagram

    Given two string s and t, reutrn if t is an anagram of s, and false otherwise

"""
from Day1ContainDup import SolutionContain as sort


class SolutionDiagram:
    def Anagram(self, s,t):
        if len(s) != len(t):
            return False
        sortedS, sortedT = [], []
        # I use ASCII as basis 
        for i in range(0 , len(s)):
            sortedS.append(ord(s[i].lower()) - (ord('a') - 1))
            sortedT.append(ord(t[i].lower()) - (ord('a') - 1))

        # used my own Sorting algo from Day 1
        return sort.Sort(sortedS) == sort.Sort(sortedT)

