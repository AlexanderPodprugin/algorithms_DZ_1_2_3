def getMinimumDifference(root): 

        if root == None: #Если пустое вернуть 0 

            return 0 

        min_d = 100000 

        stack = [root] # создаем стак с root 

        while stack: # обход стака 

            cur_vertex = stack.pop()# Получаем вершины 

            cur_stack = [cur_vertex]#записываем в еще один стак вершину и значение в root_vertex_val 

            root_vertex_val = cur_vertex.val 

            while cur_stack: #Обход по второму стаку 

                cur_vertex_two = cur_stack.pop()# получаем вершину 

  

                if cur_vertex_two.left != None: #Если не пустое записываем модуль разницы переменных  

                    cur_d = abs(root_vertex_val - cur_vertex_two.left.val) 

                    if cur_d < min_d: # если cur_d < min_d, то min_d = cur_d 

                        min_d = cur_d 

                    cur_stack.append(cur_vertex_two.left)# добавляем вершину 

                 

                if cur_vertex_two.right != None: #Если не пустое записываем модуль разницы переменных 

                    cur_d = abs(root_vertex_val - cur_vertex_two.right.val) 

                    if cur_d < min_d: # если cur_d < min_d, то min_d = cur_d 

                        min_d = cur_d 

                    cur_stack.append(cur_vertex_two.right) # добавляем вершину 

         

            if cur_vertex.left != None:# Если не пустая переменная, то добавить в стак левую вершину 

                stack.append(cur_vertex.left) 

             

            if cur_vertex.right != None: # Если не пустая переменная, то добавить в стак правую вершину 

                stack.append(cur_vertex.right) 

         

        return min_d 

  

        """Сложность O(n)"""