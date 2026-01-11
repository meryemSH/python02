def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validate the health conditions of a plant.

    Args:
        plant_name (str): Name of the plant; cannot be empty.
        water_level (int or float): Water level for the plant (1-10).
        sunlight_hours (int or float): Hours of sunlight (2-12).

    Raises:
        ValueError: If any of the conditions are violated.

    Returns:
        str: Success message if the plant is healthy.
    """
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
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """
    Test the check_plant_health function with various inputs.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print("Error:", e)

    print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print("Error:", e)

    print()

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print("Error:", e)

    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print("Error:", e)

    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
