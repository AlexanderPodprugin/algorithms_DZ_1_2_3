def hasCycle(self, head): # создаем функцию 
    slow, fast = head, head # сначала head записываем в slow, потом head записываем в fast
    while fast and fast.next: # если настоящий и след fast не пустые 
        slow = slow.next # то передвигаем slow на след узел
        fast = fast.next.next # а fast передвигаем на 2 узла вперед
        if slow == fast: # если slow и fast на одном узле
            return True # то возвращаем true
    return False # иначе возвращаем значение false 