class Motor:
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed

class Spindle:
    def __init__(self, name, power, speed, max_load):
        self.name = name
        self.power = power
        self.speed = speed
        self.max_load = max_load

class LinearAxis:
    def __init__(self, name, travel, max_speed, acceleration):
        self.name = name
        self.travel = travel
        self.max_speed = max_speed
        self.acceleration = acceleration

class RotaryAxis:
    def __init__(self, name, travel, max_speed, acceleration):
        self.name = name
        self.travel = travel
        self.max_speed = max_speed
        self.acceleration = acceleration

class Controller:
    def __init__(self, name, num_axes, max_feedrate):
        self.name = name
        self.num_axes = num_axes
        self.max_feedrate = max_feedrate









"""
        
        class LinearAxis:
    def __init__(self, name, max_speed, max_acceleration):
        self.name = name
        self.max_speed = max_speed
        self.max_acceleration = max_acceleration
        
    def move_to(self, position):
        print(f"Moving {self.name} axis to position {position}...")
        # code to actually move the axis
        
    def set_speed(self, speed):
        print(f"Setting {self.name} axis speed to {speed}...")
        # code to set the axis speed
        
class RotaryAxis:
    def __init__(self, name, max_speed, max_acceleration):
        self.name = name
        self.max_speed = max_speed
        self.max_acceleration = max_acceleration
        
    def rotate_to(self, angle):
        print(f"Rotating {self.name} axis to angle {angle}...")
        # code to actually rotate the axis
        
    def set_speed(self, speed):
        print(f"Setting {self.name} axis speed to {speed}...")
        # code to set the axis speed

class Spindle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        
    def turn_on(self):
        print(f"Turning on {self.name} spindle...")
        # code to turn on the spindle
        
    def turn_off(self):
        print(f"Turning off {self.name} spindle...")
        # code to turn off the spindle
        
    def set_speed(self, speed):
        print(f"Setting {self.name} spindle speed to {speed}...")
        # code to set the spindle speed
        
class ToolChanger:
    def __init__(self, name, num_tools):
        self.name = name
        self.num_tools = num_tools
        self.current_tool = 0
        
    def get_tool(self, tool_num):
        print(f"Retrieving tool {tool_num} from {self.name} tool changer...")
        self.current_tool = tool_num
        # code to retrieve the tool
        
    def put_tool(self):
        print(f"Returning tool {self.current_tool} to {self.name} tool changer...")
        self.current_tool = 0
        # code to return the tool

        """