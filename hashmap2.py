# Collision handling in Hashmap / HashTable:

# 1.separate chaining (open hashing):
# > This technique creates a linked list to the slot for which collision occurs.
# > > The new key is then inserted in the linked list.
# > > > These linked lists to the slots appear like chains.
# > > > > That is why, this technique is called as separate chaining.

# for searching time complexity is O(1) on worst case time complexity O(n).
# for deletion time complexity in O(n).

# 2.Open Addressing (closed hashing)
# > Liner Probing
# > > Quadratic Probing
# > > > Double hashing