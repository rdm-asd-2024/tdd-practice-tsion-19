class MoonRover:
    def __init__(self, grid_size):
        self.grid = [[0] * grid_size for _ in range(grid_size)]
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        self.x, self.y = 0, 0  # Initial position
        self.direction = 0  # Initial direction (right)
        self.route = []  # To store the route

    def move(self, command):
        if command == 'R':
            self.direction = (self.direction + 1) % 4  # Rotate right
        elif command == 'L':
            self.direction = (self.direction - 1) % 4  # Rotate left
        elif command == 'U':
            self._move_to(3)  # Move up
        elif command == 'D':
            self._move_to(2)  # Move down
        elif command == 'F':
            self._move_forward()
        elif command == 'W':
            self._move_backward()
        else:
            raise ValueError("Invalid command")

    def _move_to(self, new_direction):
        new_x, new_y = self.x + self.directions[new_direction][0], self.y + self.directions[new_direction][1]
        if self._is_valid_move(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.direction = new_direction
            self.route.append((self.x, self.y))

    def _move_forward(self):
        new_x, new_y = self.x + self.directions[self.direction][0], self.y + self.directions[self.direction][1]
        if self._is_valid_move(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.route.append((self.x, self.y))

    def _move_backward(self):
        new_direction = (self.direction + 2) % 4  # Opposite direction
        new_x, new_y = self.x + self.directions[new_direction][0], self.y + self.directions[new_direction][1]
        if self._is_valid_move(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.direction = new_direction
            self.route.append((self.x, self.y))

    def _is_valid_move(self, new_x, new_y):
        if 0 <= new_x < len(self.grid) and 0 <= new_y < len(self.grid[0]) and self.grid[new_x][new_y] != 1:
            return True
        else:
            raise Exception("Obstacle detected")

    def draw_route(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (i, j) == (self.x, self.y):
                    print('R', end=' ')
                elif (i, j) in self.route:
                    print('.', end=' ')
                else:
                    print(' ', end=' ')
            print()
rover = MoonRover(10)  # Assuming a 10x10 grid
rover.move('F')
rover.move('R')
rover.move('F')
rover.move('D')
rover.move('F')
rover.move('L')
rover.move('F')
rover.draw_route()
