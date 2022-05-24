Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
temp = temp2 = dummy = ListNode(0)
        temp.next = head
        
        while temp and temp.next:
            temp = temp.next
            if n <= 0:
                temp2 = temp2.next
            n = n-1
        temp2.next = temp2.next.next
        return dummy.next