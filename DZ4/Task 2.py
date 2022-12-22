def getMinimumDifference(root):
        if root == None:
            return 0
        min_d = 100000
        stack = [root]
        while stack:
            cur_vertex = stack.pop()
            cur_stack = [cur_vertex]
            root_vertex_val = cur_vertex.val
            while cur_stack:
                cur_vertex_two = cur_stack.pop()

                if cur_vertex_two.left != None:
                    cur_d = abs(root_vertex_val - cur_vertex_two.left.val)
                    if cur_d < min_d:
                        min_d = cur_d
                    cur_stack.append(cur_vertex_two.left)
                
                if cur_vertex_two.right != None:
                    cur_d = abs(root_vertex_val - cur_vertex_two.right.val)
                    if cur_d < min_d:
                        min_d = cur_d
                    cur_stack.append(cur_vertex_two.right)
        
            if cur_vertex.left != None:
                stack.append(cur_vertex.left)
            
            if cur_vertex.right != None:
                stack.append(cur_vertex.right)
        
        return min_d

        """Сложность O(n)"""