def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Floyd's Algorithm
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True;
        return False
