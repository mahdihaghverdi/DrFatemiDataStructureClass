from DSP import SinglyLinkedList

ll = SinglyLinkedList()
ll.append("Amirreza")
ll.append("Mahdi")
ll.appendleft("Sajad")
print(ll, end="\n\n")

for node in ll:
    print(node)

print(ll[0])
print(ll[-1])

print(ll.head, ll.tail)
print(ll.head.next_item.next_item)

print(len(ll))
print(ll[-2])

print("Mahdi" in ll)
