"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*number_wagon):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    list_wagon = []
    for index in range(0, len(number_wagon)):
        list_wagon.append(number_wagon[index])
    return list_wagon

# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    final_list = []

    first, second, *final = each_wagons_id
    
    final.remove(1)
    final_list.append(1)
    
    for index in range(0, len(missing_wagons)):
        final_list.append(missing_wagons[index])

    for index in range(0, len(final)):
        final_list.append(final[index])

    final_list.append(first)
    final_list.append(second)

    return final_list

# TODO: define the 'add_missing_stops()' function
def add_missing_stops(*args, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    dict_final = args[0]
    stop_list = []
    for chave, valor in kwargs.items():
        stop_list.append(valor)
    dict_final["stops"] = stop_list
    return dict_final


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
    #first_color = wagons_rows[0][0][1]
    #second_color = wagons_rows[0][1][1]
    #third_color = wagons_rows[0][2][1]
    
    list_0 = []
    list_1 = []
    list_2 = []
    list_all = []

    #monta saída
    for row in wagons_rows:
        for index,wagon in enumerate(row):
            if index == 0:
                list_0.append(wagon)
            if index == 1:
                list_1.append(wagon)
            if index == 2:
                list_2.append(wagon)
    list_all.append(list_0)
    list_all.append(list_1)
    list_all.append(list_2)

    return list_all

#print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))

#print(add_missing_stops({"from": "New York", "to": "Miami"},
#                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                      stop_4="Jacksonville", stop_5="Orlando"))

#print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))

#print(fix_wagon_depot([
#                    [(2, "red"), (4, "red"), (8, "red")],
#                    [(5, "blue"), (9, "blue"), (13,"blue")],
#                    [(3, "orange"), (7, "orange"), (11, "orange")],
#                    ]))