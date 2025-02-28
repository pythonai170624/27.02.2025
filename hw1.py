from hw2 import *

def main_processing_function():
    """Main function that calls all other functions."""
    print("Starting processing...")

    # Call the light computation
    result1 = light_computation(2000)
    print(f"Light computation result: {result1}")

    # Call the small list creation
    small_list = create_small_list(3000)
    print(f"Small list first 5 elements: {small_list[:5]}")

    # Call the memory heavy function
    heavy_result = calc_log_function()
    print(f"Heavy function result: {heavy_result}")

    # Call another light function
    light_result = another_function(15)
    print(f"Another light function result size: {len(light_result)}")

    print("Processing complete!")
    return "Success"

main_processing_function()