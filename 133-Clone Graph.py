"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs
        if not node:
            return None
        dt = {}     # 旧node->新node
        newNode = Node(node.val,[])
        dt[node] = newNode
        queue = [node]  # 检查队列
        i = 0
        while i < len(queue):
            for nb in queue[i].neighbors:
                if nb not in dt:
                    newNode = Node(nb.val,[])
                    dt[nb] = newNode
                    queue.append(nb)
                dt[queue[i]].neighbors.append(dt[nb])
            i += 1
            #print(i,len(queue))
        return dt[node]

        # dfs
        '''
        dt = {}
        def dfs(node):
            if node in dt:
                return dt[node]
            newNode = Node(node.val,[])
            dt[node] = newNode
            for nb in node.neighbors:
                newNode.neighbors.append(dfs(nb))
            return newNode
        
        return dfs(node)
        '''