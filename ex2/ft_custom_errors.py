class GardenError(Exception):
    """Base error for all garden problems."""
    def __init__(self, message):
        """
        Initialize a GardenError.
        """
        super().__init__(message)


class PlantError(GardenError):
    """Error for plant-related problems."""
    pass


class WaterError(GardenError):
    """Error for watering-related problems."""
    pass


def check_plant(plant_name, healthy):
    """
    Check the health of a plant and raise PlantError if unhealthy.

    Args:
        plant_name (str): Name of the plant.
        healthy (bool): True if the plant is healthy, False otherwise.

    Raises:
        PlantError: If the plant is unhealthy.
    """
    if not healthy:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(tank_level):
    """
    Check the water level and raise WaterError if insufficient.
    Raises:
        WaterError: If water level is less than 1.
    """
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
