##################################################################
# University Map Project - A_Star_Algorithm
# Tools: python
##################################################################
#               A Star Search Algorithm
# The A* search algorithm is the most widely and the best
# search algorithm. which is used to find paths that can be
# taken to traverse from one point to another, by finding the
# shortest path between two points. It evaluates nodes by
# combining g(n) gives the path cost from the start node to
# node n , and h(n) is the estimated cost of the cheapest path
# from n to the goal , we have f(n) is estimated cost of the
# cheapest solution through n .
# f(n) = g(n) + h(n)
##################################################################


from collections import deque

# connect (secondScreen) to this file
import secondScreen

# take the start point from the previous screen
print(secondScreen.start)
start = secondScreen.start

# take the start point from the previous screen
print(secondScreen.end)
end = secondScreen.end


class Algorithm:
    print("Algorithm")

    def __init__(self, MapList):
        print("Algorithm/--int--")
        self.MapList = MapList

    def get_neighbors(self, v):
        print("Algorithm/get_neighbors")
        return self.MapList[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        print("Algorithm/h")
        heuristic = {
            "Gate 2": 1,
            'Gate 3': 1,
            '(11) College of Computer': 1,
            'Kindergarten building': 1,
            '(5) College of Science': 1,
            '(3) College of Sport': 1,
            '(1) College of Humanities': 1
        }

        return heuristic[n]

    def a_star_algorithm(self, start_node, stop_node):
        print("Algorithm/a_star_algorithm")
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


print("Start" + start)


def get_DirectionList():
    return DirectionList


# Data class, contain the data for "University of jeddah" map
class Data:
    print("Data")
    # data
    adjacency_list = {
        "Gate 2": [("Gate 3", 190), ("(5) College of Science", 110), ("(3) College of Sport", 116),
                   ("(1) College of Humanities", 120)],

        "Gate 3": [("(11) College of Computer", 130), ("Kindergarten building", 65), ("(5) College of Science", 104), ("Gate 2", 190)],

        "(11) College of Computer": [("Gate 3", 130), ("Kindergarten building", 90), ("(5) College of Science", 240)],

        "Kindergarten building": [("(11) College of Computer", 90), ("Gate 3", 65), ("(5) College of Science", 165)],

        "(5) College of Science": [("(11) College of Computer", 240), ("Kindergarten building", 165), ("Gate 3", 104), ("Gate 2", 110),
                                   ("(1) College of Humanities", 95), ("(3) College of Sport", 50)],

        "(3) College of Sport": [("(5) College of Science", 50), ("Gate 2", 116), ("(1) College of Humanities", 50)],

        "(1) College of Humanities": [("(3) College of Sport", 50), ("(5) College of Science", 95), ("Gate 2", 120)]
    }

    # input
    graph1 = Algorithm(adjacency_list)
    global DirectionList
    DirectionList = graph1.a_star_algorithm(start, end)
    global Postion
    Postion = "FROM " + start + " TO " + end
    print(Postion)

