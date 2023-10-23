class MoonRover:
    def __init__(self, obstacles=[]):
        self.x = 0
        self.y = 0
        self.direction = 'N'  # Initial direction: North
        self.obstacles = set(obstacles)
        self.route = []

    def move(self, commands):
        for command in commands:
            if command == 'R':
                self.rotate_right()
            elif command == 'L':
                self.rotate_left()
            elif command == 'U':
                self.move_up()
            elif command == 'D':
                self.move_down()
            elif command == 'F':
                self.move_forward()
            elif command == 'W':
                self.move_backward()
            else:
                raise ValueError(f"Invalid command: {command}")
    
    def rotate_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'
    
    def rotate_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
    
    def move_up(self):
        new_y = self.y + 1
        if self.check_obstacle(self.x, new_y):
            raise Exception("Obstacle detected")
        self.y = new_y
        self.route.append((self.x, new_y))
    
    def move_down(self):
        new_y = self.y - 1
        if self.check_obstacle(self.x, new_y):
            raise Exception("Obstacle detected")
        self.y = new_y
        self.route.append((self.x, new_y))
    
    def move_forward(self):
        new_x, new_y = self.calculate_forward_position()
        if self.check_obstacle(new_x, new_y):
            raise Exception("Obstacle detected")
        self.x = new_x
        self.y = new_y
        self.route.append((new_x, new_y))
    
    def move_backward(self):
        new_x, new_y = self.calculate_backward_position()
        if self.check_obstacle(new_x, new_y):
            raise Exception("Obstacle detected")
        self.x = new_x
        self.y = new_y
        self.route.append((new_x, new_y))

    def calculate_forward_position(self):
        if self.direction == 'N':
            return self.x, self.y + 1
        elif self.direction == 'E':
            return self.x + 1, self.y
        elif self.direction == 'S':
            return self.x, self.y - 1
        elif self.direction == 'W':
            return self.x - 1, self.y

    def calculate_backward_position(self):
        if self.direction == 'N':
            return self.x, self.y - 1
        elif self.direction == 'E':
            return self.x - 1, self.y
        elif self.direction == 'S':
            return self.x, self.y + 1
        elif self.direction == 'W':
            return self.x + 1, self.y
    
    def check_obstacle(self, x, y):
        return (x, y) in self.obstacles

    def print_route(self):
        for x, y in self.route:
            print(f"({x}, {y})")
obstacles = [(1, 1), (2, 2)]
rover = MoonRover(obstacles)

try:
    rover.move("FRFFL")  # Example commands
except Exception as e:
    print(e)

rover.print_route()  # Print the route the rover has followed
