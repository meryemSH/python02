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


def check_plant(plant_name, healthy):
    """Raise PlantError if the plant is unhealthy."""
    if not healthy:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(tank_level):
    """Raise WaterError if water is insufficient."""
    if tank_level < 1:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato", False)
    except PlantError as e:
        print("Caught PlantError:", e)
    print()

    print("Testing WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print("Caught WaterError:", e)
    print()
    print("Testing catching all garden errors...")

    try:
        check_plant("tomato", False)
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_water(0)
    except GardenError as e:
        print("Caught a garden error:", e)
    print()
    print("All custom error types work correctly!")
