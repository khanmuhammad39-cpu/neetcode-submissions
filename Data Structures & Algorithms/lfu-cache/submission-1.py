class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        self.frequency = 1


class LinkedList:
    def __init__(self):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        # near the head = least recent within the same frequency
        # near the tail = most recent within the same frequency
    
    def add_node_tail(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None
    
    def isEmpty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_list = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.update_frequency(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update_frequency(node)
            return

        if len(self.key_to_node) >= self.capacity:
            self.remove_left()

        new_node = ListNode(key, value)
        self.key_to_node[key] = new_node

        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = LinkedList()

        self.freq_to_list[1].add_node_tail(new_node)
        self.min_freq = 1
    
    def update_frequency(self, node):
        old_freq = node.frequency
        self.freq_to_list[old_freq].remove(node)

        if self.freq_to_list[old_freq].isEmpty():
            del self.freq_to_list[old_freq]
            if self.min_freq == old_freq:
                self.min_freq += 1
        
        node.frequency += 1
        new_freq = node.frequency

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = LinkedList()
        
        self.freq_to_list[new_freq].add_node_tail(node)
    
    def remove_left(self):
        linked_list = self.freq_to_list[self.min_freq]
        node_to_remove = linked_list.head.next
        linked_list.remove(node_to_remove)

        if linked_list.isEmpty():
            del self.freq_to_list[self.min_freq]

        del self.key_to_node[node_to_remove.key]