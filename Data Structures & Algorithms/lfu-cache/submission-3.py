# Structure
# key node pair -> to get the node quickly where key is a unique_id
# freq linkedlist pair -> for the same frequency what nodes have the same freq
# on the left side least recent (head)
# on the right side most recent
# the ListNode will have freq also (default = 1)


class ListNode:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        self.freq = 1 # default

class LinkedList:
    # initializing the object
    def __init__(self):
        self.head = ListNode(None,None)
        self.tail = ListNode(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    #adding a node to the tail
    def add_node(self,node):
        # A -> tail to A -> node -> tail
        A = self.tail.prev
        # deal with A first
        A.next = node
        node.prev = A
        # deal with tail
        node.next = self.tail
        self.tail.prev = node
    
    # remove the node least recent
    def remove_node(self,node):
        # A -> node -> B to A -> B
        A = node.prev
        B = node.next
        # deal with A and B
        A.next = B
        B.prev = A
        # remove the node
        node.next = None
        node.prev = None
    
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
        # update the node freq
        self.update_freq(key)
        val = node.val
        return val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update_freq(key)
            return
        
        if self.capacity == len(self.key_to_node):
            linked_list = self.freq_to_list[self.min_freq]
            node_to_remove = linked_list.head.next
            linked_list.remove_node(node_to_remove)
            del self.key_to_node[node_to_remove.key]
        
        new_node = ListNode(value, key)
        self.key_to_node[key] = new_node
        
        if 1 not in self.freq_to_list:
            linked_list_min = LinkedList()
            self.min_freq = 1
            linked_list_min.add_node(new_node)
            self.freq_to_list[1] = linked_list_min
            return
        
        self.freq_to_list[1].add_node(new_node)
        self.min_freq = 1
        return


    
    # if used for get and put we update nodes freq
    # and push into the linked list having its freq
    def update_freq(self,key):
        node = self.key_to_node[key]
        freq = node.freq
        
        old_list = self.freq_to_list[freq]
        old_list.remove_node(node)

        if freq == self.min_freq:
            if old_list.isEmpty():
                self.min_freq += 1

        freq += 1
        node.freq += 1
        if freq not in self.freq_to_list:
            self.freq_to_list[freq] = LinkedList()
            self.freq_to_list[freq].add_node(node)
        else:
            self.freq_to_list[freq].add_node(node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)