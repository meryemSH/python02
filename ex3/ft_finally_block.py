def water_plants(plant_list):
    """
    Water a list of plants, handling errors and always performing cleanup.

    Args:
        plant_list (list): List of plant names (str) to water.
                           None represents an invalid plant.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the water_plants function with normal and error scenarios.
    """
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__maine__":
    test_watering_system()
