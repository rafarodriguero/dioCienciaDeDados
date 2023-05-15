"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*number_wagon):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    return list(number_wagon)

# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    first, second, *final = each_wagons_id
    final.remove(1)    

    return [1, *missing_wagons, *final, first, second]

# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    return {**route, "stops": list(kwargs.values())}


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    return list(map(list, zip(*wagons_rows)))

#print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

#print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))

#print(add_missing_stops({"from": "New York", "to": "Miami"},
#                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                      stop_4="Jacksonville", stop_5="Orlando"))

#print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))

#print(fix_wagon_depot([
#                    [(2, "red"), (4, "red"), (8, "red")],
#                    [(5, "blue"), (9, "blue"), (13,"blue")],
#                    [(3, "orange"), (7, "orange"), (11, "orange")],
#                    ]))
