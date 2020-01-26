"""Vehicles Routing Problem (VRP)."""
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def _return_solution(_data: dict, _manager, _routing, _solution) -> dict:
    """ Returns solution as a dict."""
    output_dict = {}
    for vehicle_id in range(_data['num_vehicles']):
        index = _routing.Start(vehicle_id)
        plan_output = []
        route_distance = 0
        while not _routing.IsEnd(index):
            plan_output.append(_manager.IndexToNode(index))
            previous_index = index
            index = _solution.Value(_routing.NextVar(index))
            route_distance += _routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output.append(_manager.IndexToNode(index))
        output_dict[f'Vehicle ID {vehicle_id}'] = {'Route': plan_output, 'Distance': route_distance}
    output_dict['Status'] = 'Success'
    return output_dict


def vrp_solve(user_data: dict) -> dict:
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    # data = create_data_model()
    data = user_data

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Returns solution if one is found
    if solution:
        return _return_solution(data, manager, routing, solution)
    else:
        return {'Message': 'No solution', 'Status': 'Failure'}
