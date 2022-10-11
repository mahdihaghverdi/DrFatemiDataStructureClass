import pprint

from DSP import SinglyLinkedList

ll = SinglyLinkedList()
ll.append("Amirreza")
ll.append("Mahdi")
ll.appendleft("Sajad")
ll.insert(1, "Amirrrrr")
print(ll)
ll.insert(2, "Zohre")
print(ll)
ll.insert(3, "Sina")
print(ll)

ll.insert(0, 11)
print(ll)
