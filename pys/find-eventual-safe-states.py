from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNodes = []

        for i, node in enumerate(graph):
            if len(node) == 0:
              safeNodes.append(i)
              continue
            
            