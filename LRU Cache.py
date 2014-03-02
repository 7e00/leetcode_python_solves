class LRUCache:
    class KeyNode:
        def __init__(self, key):
            self.val = key
            self.pre = -1
            self.next = -1

    # @param capacity, an integer
    def __init__(self, capacity):
        self.volume = capacity
        self.num = 0
        self.keys = []
        self.head = 0
        self.tail = 0
        self.dic = {}

    # @return an integer
    def get(self, key):
        if key in self.dic:
            value, pos = self.dic[key]
            self.keys[self.keys[pos].pre].next = self.keys[pos].next
            self.keys[self.keys[pos].next].pre = self.keys[pos].pre
            if pos == self.head:
                self.head = self.keys[pos].next
            if pos == self.tail:
                self.tail = self.keys[pos].pre
            self.keys[self.head].pre = self.tail
            self.keys[self.tail].next = self.head
            self.keys[pos].pre = self.tail
            self.keys[pos].next = self.keys[self.tail].next
            self.keys[self.tail].next = pos
            self.keys[self.head].pre = pos
            self.tail = pos
            return value
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.dic:
            if self.num == self.volume:
                del self.dic[self.keys[self.head].val]
                free = self.head
                self.head = self.keys[self.head].next
                self.keys[self.head].pre = self.keys[free].pre
                self.keys[free].val = key
                self.keys[free].pre = self.tail
                self.keys[free].next = self.head
                self.keys[self.tail].next = free
                self.keys[self.head].pre = free
                self.tail = free
            else:
                self.num += 1
                self.keys.append(LRUCache.KeyNode(key))
                self.keys[len(self.keys)-1].pre = self.tail
                self.keys[len(self.keys)-1].next = self.head
                self.keys[self.tail].next = len(self.keys)-1
                self.keys[self.head].pre = len(self.keys)-1
                self.tail = len(self.keys) - 1
            self.dic[key] = [value, self.tail]
        else:
            t = self.dic[key]
            t[0] = value
            pos = t[1]
            self.keys[self.keys[pos].pre].next = self.keys[pos].next
            self.keys[self.keys[pos].next].pre = self.keys[pos].pre
            if pos == self.head:
                self.head = self.keys[pos].next
            if pos == self.tail:
                self.tail = self.keys[pos].pre
            self.keys[self.head].pre = self.tail
            self.keys[self.tail].next = self.head
            self.keys[pos].pre = self.tail
            self.keys[pos].next = self.keys[self.tail].next
            self.keys[self.tail].next = pos
            self.keys[self.head].pre = pos
            self.tail = pos