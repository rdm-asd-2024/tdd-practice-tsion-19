class MoonRover:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = 'N'  # Start by facing North
        self.commands = {
            'R': self.rotate_right,
            'L': self.rotate_left,
            'U': self.move_up,
            'D': self.move_down
        }
        self.obstacles = set()  # You can add obstacle coordinates here

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

    def execute_command(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            raise ValueError("Invalid command")

    def switch_guide_system(self, system):
        if system == 'FLFW':
            self.commands = {
                'R': self.rotate_right,
                'L': self.rotate_left,
                'F': self.move_forward,
                'W': self.move_backward
            }
        else:
            self.commands = {
                'R': self.rotate_right,
                'L': self.rotate_left,
                'U': self.move_up,
                'D': self.move_down
            }

    def move_forward(self):
        if self.direction == 'N':
            self.move_up()
        elif self.direction == 'E':
            self.move_right()
        elif self.direction == 'S':
            self.move_down()
        else:
            self.move_left()

    def move_backward(self):
        if self.direction == 'N':
            self.move_down()
        elif self.direction == 'E':
            self.move_left()
        elif self.direction == 'S':
            self.move_up()
        else:
            self.move_right()

    def draw_route(self):
        print(f"Rover's current position: ({self.x}, {self.y})")
        print(f"Rover's current direction: {self.direction}")


# Example usage:
rover = MoonRover()
rover.execute_command('R')
rover.execute_command('U')
rover.execute_command('L')
rover.draw_route()
