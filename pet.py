class Pet:
    def __init__(self, name, hunger, energy, happiness, tricks):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = tricks

    def get_status(self):
        print(f"Name: {self.name}, Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

    def show_tricks(self):
        print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")

    def eat(self):
        self.hunger = max(0, self.hunger - 1)
        self.happiness += 1
        print(f"{self.name} ate some food. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def play(self):
        self.energy = max(0, self.energy - 1)
        self.happiness += 2
        self.hunger += 1
        print(f"{self.name} played. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def sleep(self):
        self.energy += 3
        print(f"{self.name} slept. Energy: {self.energy}")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness += 1
        print(f"{self.name} learned a new trick: {trick}. Happiness: {self.happiness}")