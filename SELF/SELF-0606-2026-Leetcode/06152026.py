# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

#TJS: seems obscure ... thus not attempted

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        out_list=[]
        for n in list1:
            out_list.append(n)
        for n in list2:
            out_list.append(n)
            
        return sorted(out_list)        
        
my_object = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(my_object.mergeTwoLists(list1=list1,list2=list2))