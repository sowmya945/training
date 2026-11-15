from abc import ABC, abstractmethod

# 1. ABSTRACTION: Define an abstract base class for all robots
class Robot(ABC):
    def __init__(self, name, model, battery_level=100):
        self.name = name                # Public attribute
        self.model = model              # Public attribute
        self.__battery_level = battery_level  # 2. ENCAPSULATION: Private attribute

    # Getter method to safely access the private battery attribute
    def get_battery(self):
        return f"{self.__battery_level}%"

    # Setter method to safely update battery level with validation
    def charge(self, amount):
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"{self.name} charged. Current battery: {self.get_battery()}")

    # Abstract method: Every subclass MUST implement its own version
    @abstractmethod
    def perform_task(self):
        pass

    # Shared method across all robots
    def introduce(self):
        print(f"Hello! I am {self.name}, a {self.model} robot.")
        print(f"My current battery level is {self.get_battery()}.")
        self.perform_task()
        print("-" * 40)


# 3. INHERITANCE: Child classes inherit attributes and methods from Robot
class ExplorerRobot(Robot):
    def __init__(self, name, model, terrain_type):
        super().__init__(name, model)  # Inherit parent constructor
        self.terrain_type = terrain_type

    # 4. POLYMORPHISM: Overriding perform_task() for an explorer robot
    def perform_task(self):
        print(f"Specialty: Navigating {self.terrain_type} terrain and mapping new areas.")


class AssistantRobot(Robot):
    def __init__(self, name, model, language):
        super().__init__(name, model)
        self.language = language

    # 4. POLYMORPHISM: Overriding perform_task() for an assistant robot
    def perform_task(self):
        print(f"Specialty: Assisting humans and speaking fluent {self.language}.")


# --- Instantiating Objects and Running the Program ---
if __name__ == "__main__":
    # Creating robot objects (instances)
    rover = ExplorerRobot(name="Atlas-X", model="Rover V2", terrain_type="Martian rocky")
    helper = AssistantRobot(name="Nova", model="HomeMate 3000", language="English")

    # Storing different robot types in a single list
    robots = [rover, helper]

    # Calling the same method on different objects produces specialized output
    for bot in robots:
        bot.introduce()
