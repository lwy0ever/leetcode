\u0022\u0022\u0022\u000A# Definition for a Node.\u000Aclass Node:\u000A    def __init__(self, val, neighbors):\u000A        self.val \u003D val\u000A        self.neighbors \u003D neighbors\u000A\u0022\u0022\u0022\u000Aclass Solution:\u000A    def cloneGraph(self, node: \u0027Node\u0027) \u002D\u003E \u0027Node\u0027:\u000A        # bfs\u000A        if not node:\u000A            return None\u000A        dt \u003D {}     # 旧node\u002D\u003E新node\u000A        newNode \u003D Node(node.val,[])\u000A        dt[node] \u003D newNode\u000A        queue \u003D [node]  # 检查队列\u000A        i \u003D 0\u000A        while i \u003C len(queue):\u000A            for nb in queue[i].neighbors:\u000A                if nb not in dt:\u000A                    newNode \u003D Node(nb.val,[])\u000A                    dt[nb] \u003D newNode\u000A                    queue.append(nb)\u000A                dt[queue[i]].neighbors.append(dt[nb])\u000A            i +\u003D 1\u000A            #print(i,len(queue))\u000A        return dt[node]\u000A\u000A        # dfs\u000A        \u0027\u0027\u0027\u000A        dt \u003D {}\u000A        def dfs(node):\u000A            if node in dt:\u000A                return dt[node]\u000A            newNode \u003D Node(node.val,[])\u000A            dt[node] \u003D newNode\u000A            for nb in node.neighbors:\u000A                newNode.neighbors.append(dfs(nb))\u000A            return newNode\u000A        \u000A        return dfs(node)\u000A        \u0027\u0027\u0027