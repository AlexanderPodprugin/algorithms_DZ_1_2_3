def isPalindrome(self, head): # создаем функцию
    for_ans = [] # создаем путой список
    while head.next: # пока голова не пустая 
        for_ans.append(head.val) # добавляем значение головы в список
        head = head.next # перемещаем голову в след узел
    for_ans.append(head.val) # добавляем последнее значение очереди а список 
    return for_ans == for_ans[::-1]# проверяем является ли список полиндромом


    """O(n)"""