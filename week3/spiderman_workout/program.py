from sys import stdin as inp 

class Node:
    max_building = 0
    def __init__(self, value, direction, level):
        self.value = value
        self.direction = direction
        self.level = level
        self.path_height = value # to start with 
        self.up = None
        self.down = None
        self.from_up = None
        self.from_down = None
        self.at_input = 0
    
   # @classmethod
    #def set_max_building(cls, height):
        #cls.max_building = height


    def add(self, h):
        if self.value + h < self.max_building:
            self.up = Node(self.value + h, 'U', self.level + 1)
            self.up.at_input = h
            self.up.from_up = self
            self.up.path_height = self.path_height + h
            # self.adjust_path_height()

        if self.value - h >= 0:
            self.down = Node(self.value - h, 'D', self.level + 1)
            self.down.from_down = self

   # def adjust_path_height(self):
        #last = self.from_up
        #while last:
            #last.path_height = self.path_height
            #last = last.from_up


    def __bool__(self):
        return self.value != None

    def __lt__(self, other):
        return self.path_height < other.path_height


class Dag:
    def __init__(self, initial):
        self.initial = initial
        self.last = []
        self.nodes = [initial]


    def get_nodes_by_level(self, level):
        return [node for node in self.nodes if node.level == level]

    def add(self, node):
        self.nodes.append(node)



def solve(m, heights):
    if len(set(heights)) == 1:
        print('UD'*(m//2))
        return

    # print(heights)
    initial = Node(heights[0], 'U', 0)
    Node.max_building = sum(heights) // 2 + 1
    dag = Dag(initial)

    level = 0
    for h in heights[1:]:
        nodes = dag.get_nodes_by_level(level)
        while nodes:
            node = nodes.pop()
            node.add(h)
            if node.up:
                dag.add(node.up)
            if node.down:
                dag.add(node.down)
        level += 1

    #print(level)

    l = (dag.get_nodes_by_level(level))
    #print(dag.nodes)

    string = 'D'
    k = [node for node in l if node.value == 0]
    if not k:
        print('IMPOSSIBLE')
        return
    if k:
        start = min(k)
        while start.from_up or start.from_down:
            if not start.from_up:
                start = start.from_down
            elif not start.from_down:
                start = start.from_up
            else:
                start = min(start.from_down, start.from_up)
            string += start.direction

    print(string[::-1])

        


if __name__ == '__main__':
    n = int(inp.readline().strip())
    for _ in range(n):
        m = int(inp.readline().strip())
        heights = list(map(int, inp.readline().strip().split()))
        #print('*'*10)
        solve(m, heights)
        #print('*'*10)