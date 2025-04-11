"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    Fish: list
    Bears: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""

        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Function to remove fish that died."""
        alive_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_fish.append(fish)
        self.fish = alive_fish
        alive_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                alive_bears.append(bear)
        self.bears = alive_bears

    def remove_fish(self, amount: int) -> None:
        self.fish = self.fish[amount:]

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)

        self.bears = alive_bears

    def repopulate_fish(self):
        baby_fish = len(self.fish) // 2
        while baby_fish > 0:
            self.fish.append(Fish())
            baby_fish -= 1

    def repopulate_bears(self):
        """Models reproduction in bears"""
        baby_bear = len(self.bears) // 2
        while baby_bear > 0:
            self.bears.append(Bear())
            baby_bear -= 1

    def view_river(self):
        """Prints what the current ecosytem is"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
