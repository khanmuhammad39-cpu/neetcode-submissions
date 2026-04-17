class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 1


class LinkedList:
    def __init__(self):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self, node):
        # insert right before tail
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.prev = None
        node.next = None

    def is_empty(self):
        return self.head.next == self.tail

    def pop_left(self):
        # removes least recently used node in this frequency list
        if self.is_empty():
            return None
        node = self.head.next
        self.remove_node(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_list = {}

    def update_freq(self, node):
        old_freq = node.freq
        old_list = self.freq_to_list[old_freq]
        old_list.remove_node(node)

        if old_freq == self.min_freq and old_list.is_empty():
            self.min_freq += 1

        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = LinkedList()

        self.freq_to_list[new_freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update_freq(node)
            return

        if len(self.key_to_node) == self.capacity:
            lfu_list = self.freq_to_list[self.min_freq]
            node_to_remove = lfu_list.pop_left()
            del self.key_to_node[node_to_remove.key]

        new_node = ListNode(key, value)
        self.key_to_node[key] = new_node

        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = LinkedList()

        self.freq_to_list[1].add_node(new_node)
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)