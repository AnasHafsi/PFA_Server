
from warnings import warn
import move


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  
def astar(maze, start, end, allow_diagonal_movement=False):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = []
    open_list.append(start_node)
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 2
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),
                            (-1, -1), (-1, 1), (1, -1), (1, 1),)
    while len(open_list) > 0:
        outer_iterations += 1
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        if outer_iterations > max_iterations:
            warn("giving up on pathfinding too many iterations")
            return return_path(current_node)
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            return return_path(current_node)
        children = []

        for new_position in adjacent_squares:  
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)
        for child in children:

            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue
            open_list.append(child)


def main(mz):

    st_lst = mz.split(';')
    st = st_lst[2]
    diag = st_lst[4]
    isDiag=False
    if(diag=='1') : isDiag=True
    st = st.split(" ")
    st = tuple(map(int, st))
    en = st_lst[3]
    en = en.split(" ")
    en = tuple(map(int, en))
    maze = st_lst[1]
    size = int(st_lst[0])
    cha = list(maze)
    tmp = []
    res = []
    for i in range(len(cha)+size):
        if (i % size == 0):
            tmp = list(map(int, tmp))
            if (tmp != []):
                res.append(tmp)
            tmp = []
        if(i < len(cha)):
            tmp.append(cha[i])
    maze = res
    start = st
    end = en
    path = astar(maze, start, end,isDiag)
    tst = True
    print(maze)
    print(path)
    m = 0
    while tst:
        (tst,pt)=move.main(path,m)
        if (tst):maze[pt[0]][pt[1]]=1
        path = astar(maze, start, end,isDiag)
        print(maze)
        m=1
    return path
