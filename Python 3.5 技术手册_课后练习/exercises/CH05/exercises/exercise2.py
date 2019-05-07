class Mouse:
    @staticmethod
    def go(maze, start, end):
        route = []
        Mouse.visit(maze, start, end, route)
        return route

    @staticmethod
    def visit(maze, pt, end, route):
        if Mouse.isVisitable(maze, pt, route):
            route.append(pt)
            if not Mouse.isEnd(route, end) and \
               not Mouse.tryOneOut(maze, pt, end, route):
                route.pop()
        return Mouse.isEnd(route, end)

    @staticmethod
    def isVisitable(maze, pt, route):
        return maze[pt[0]][pt[1]] == 0 and pt not in route

    @staticmethod
    def isEnd(route, end):
        return end in route

    @staticmethod
    def tryOneOut(maze, pt, end, route):
        return Mouse.visit(maze, (pt[0], pt[1] + 1), end, route) or \
               Mouse.visit(maze, (pt[0] + 1, pt[1]), end, route) or \
               Mouse.visit(maze, (pt[0], pt[1] - 1), end, route) or \
               Mouse.visit(maze, (pt[0] - 1, pt[1]), end, route)

maze = [[2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2],
        [2, 0, 0, 2, 0, 2, 2],
        [2, 2, 0, 2, 0, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 0, 2]]

for pt in Mouse.go(maze, (1, 0), (6, 5)):
    maze[pt[0]][pt[1]] = 1

if maze[5][5] == 0:
    print("找不到出口")

for row in maze:
    for block in row:
        {
            0 : lambda: print('  ', end=''),
            1 : lambda: print('◇', end=''),
            2 : lambda: print('█',end=''),
        }[block]()
    print()