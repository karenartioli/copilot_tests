def number_of_people(bus_stops):
    """
    Calculates the total number of people on the bus after all the stops.

    Args:
        bus_stops (list): A list of tuples representing the number of people getting on and off at each stop.

    Returns:
        int: The total number of people on the bus after all the stops.
    """
    total_people = 0
    for stop in bus_stops:
        total_people += stop[0] - stop[1]
    return total_people