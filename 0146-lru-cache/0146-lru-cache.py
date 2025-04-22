class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head & tail to avoid edge checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Unlink `node` from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """Insert `node` right after head (most‑recent position)."""
        first = self.head.next
        node.next = first
        node.prev = self.head
        self.head.next = node
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # This key was just used → move it to the front
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node and bump it to front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Evict the LRU item: tail.prev
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Insert the new node as most‑recent
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
