class GardenError(Exception):
    """Base error for all garden problems."""
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    """Error for plant-related problems."""
    pass


class WaterError(GardenError):
    """Error for watering-related problems."""
    pass


class SunError(GardenError):
    """Specific error for sun-related issues."""
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, plant_name, water_level, sunlight_hours):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        plant = [plant_name, water_level, sunlight_hours]
        self.plants.append(plant)

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                name, water, sun = plant
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name_to_check):
        for plant in self.plants:
            name, water, sun = plant
            if name == plant_name_to_check:

                if water > 10:
                    raise PlantError(
                        f"Water level {water} is too high (max 10)"
                        )
                if water < 1:
                    raise PlantError(f"Water level {water} is too low (min 1)")

                if sun > 12:
                    raise SunError(
                        f"Sunlight hours {sun} is too high (max 12)"
                    )
                if sun < 2:
                    raise SunError(
                        f"Sunlight hours {sun} is too low (min 2)"
                    )

                print(f"{name}: healthy (water: {water}, sun: {sun})")
                return
        raise PlantError(f"Plant '{plant_name_to_check}' does not exist")


def test_garden_management():
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plants("tomato", 5, 8)
        print("Added tomato successfully")

        manager.add_plants("lettuce", 15, 6)
        print("Added lettuce successfully")

        manager.add_plants("", 3, 5)
    except PlantError as e:
        print("Error adding plant:", e)

    print()

    print("Watering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print("Error:", e)

    print()

    print("Checking plant health...")
    for plant_name in ["tomato", "lettuce"]:
        try:
            manager.check_plant_health(plant_name)
        except GardenError as e:
            print(f"Error checking {plant_name}:", e)

    print()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
