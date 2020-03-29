class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E
    node_E.next = node_A

def insert_node(data):
    global node_A
    new_node = Node(data)  # 새로운 객체 생성
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:  # 삽입할 위치를 탐색
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node


def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    if pre_node.data == del_data:  # 삭제하고자 하는 노드가 첫번째 노드일때
        node_A = next_node
        del pre_node
        return
    while next_node:  # 삭제하고자 하는 노드가 첫번째 노드가 아닐때
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next


def print_list(data):
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
        if(node.data == data):  #무한루프 방지
            # 원형연결리스트는 반복해서 계속 돈다는것을 보여주기 위해 끝까지 출력하고 다시 돌아와서 첫번째 노드인 A까지만 출력!
            print(node.data)
            break

if __name__ == '__main__':
    print('연결 리스트 초기화 후! ')
    init_list()
    print_list('A')

    print('Node C를 추가한 후')
    insert_node("C")
    print_list('A')

    print('Node D를 삭제한 후')
    delete_node('D')
    print_list('A')
