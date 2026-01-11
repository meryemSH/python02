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
    """
    Specific error for sun-related issues .
    """
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, plant_name, water_level, sunlight_hours):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        plant = [plant_name, water_level, sunlight_hours]
        self.plants.append(plant)

    def water_plants(self, plant_name, water_level, sunlight_hours):
        print("Opening watering system")
        try:
            if water_level > 10:
                raise WaterError(
                    f"Water level {water_level} is too high (max 10)"
                    )
            if water_level < 1:
                raise WaterError(
                    f"Water level {water_level} is too low (min 1)"
                    )
            for plant in self.plants:
                print(f"Watering {plant[0]} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        return (
            f"{plant_name}: healthy"
            f" (water: {water_level}, sun: {sunlight_hours})")


def test_garden_management():
    print("=== Garden Management System Test ===")
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
    for plant_name in ["tomato", "lettuce", "cucumber"]:
        try:
            manager.check_plant_health(plant_name)
        except PlantError as e:
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
