class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next   # save the next node
            curr.next = prev  # reverse the pointer
            prev = curr       # move prev forward
            curr = nxt        # move curr forward
        return prev


# ---------- Local test helpers ----------
def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- Local test cases ----------
if __name__ == "__main__":
    sol = Solution()

    # Test 1: typical case
    assert to_list(sol.reverseList(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

    # Test 2: edge case - single element
    assert to_list(sol.reverseList(build_list([1]))) == [1]

    # Test 3: edge case - empty list
    assert to_list(sol.reverseList(build_list([]))) == []

    print("All test cases passed")