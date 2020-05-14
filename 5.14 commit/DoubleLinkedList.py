class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_B.prev = node_A
    node_D.next = node_E
    node_D.prev = node_B
    node_E.prev = node_B

def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A

    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next


    node_P.next = new_node
    new_node.prev = node_P
    new_node.next = node_T
    node_T.prev = new_node

def delete_node(data):
    global node_A
    node_prev = node_A
    node_next = node_prev.next
    node_next_next = node_next.next
    if node_prev.data == data:
        node1 = node_next
        del node_prev
        return
    while node_next:
        if node_next.data == data:
            node_prev.next = node_next_next
            node_next_next.prev = node_prev
            del node_next
            return
def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next

if __name__== '__main__':
    print('연결리스트 초기화 후')
    init_list()
    print_list()

    print('노드 C 추가 이후')
    insert_node('C')
    print_list()

    print('노드 B 삭제 이후')
    delete_node('B')
    print_list()

    print('노드 C 삭제 이후')
    delete_node('C')
    print_list()

