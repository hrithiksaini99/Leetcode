class Node:
    """A node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """LRU Cache implementation."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key-node pairs
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Add a node right after the head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Get the value of the key if the key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove from current position
            self._add_to_head(node)  # Add to head (most recently used)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Add a key-value pair to the cache."""
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the old node
        node = Node(key, value)
        self._add_to_head(node)  # Add the new node to the head
        self.cache[key] = node  # Update the cache

        if len(self.cache) > self.capacity:
            # Remove the least recently used item (the node before the tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]  # Remove from cache

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
