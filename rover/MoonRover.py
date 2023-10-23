class MoonRover:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = 'N'  # Start by facing North
        self.obstacles = set()  # You can add obstacle coordinates here

    def move(self, command):
        if command == 'R':
            self.rotate_right()
        elif command == 'L':
            self.rotate_left()
        elif command == 'U':
            self.move_up()
        elif command == 'D':
            self.move_down()
        else:
            raise ValueError("Invalid command. Only 'R', 'L', 'U', and 'D' are allowed.")

    def rotate_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        else:
            self.direction = 'N'

    def rotate_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        else:
            self.direction = 'N'

    def move_up(self):
        if (self.x, self.y + 1) not in self.obstacles:
            self.y += 1
        else:
            raise Exception("Obstacle in the way!")

    
    def move_down(self):
        if (self.x, self.y - 1) not in self.obstacles:
           self.y -= 1
        else:
            raise Exception("Obstacle in the way!")


    def execute_commands(self, commands):
        for command in commands:
            self.move(command)

    def draw_route(self):
        print(f"Rover's current position: ({self.x}, {self.y})")
        print(f"Rover's current direction: {self.direction}")


# Example usage:
rover = MoonRover()
commands = input("Enter commands (R/L/U/D): ")
try:
    rover.execute_commands(commands)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    rover.draw_route()
