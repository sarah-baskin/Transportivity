from TrainTypes import Subway
from TrainTypes import Station
from collections import defaultdict

def main():


    Alewife = Station("Alewife", "Subway and Bus")
    Davis = Station("Davis", "Subway and Bus")
    Porter = Station("Porter", "Subway and Bus")
    Harvard = Station("Harvard", "Subway and Bus")
    Central = Station("Central", "Subway and Bus")
    Kendall_MIT = Station("Kendall/MIT", "Subway and Bus")
    Charles_MGH = Station("Charles/MGH", "Subway")
    Park_Street = Station("Park Street", "Subway and Bus")
    Downtown_Crossing = Station("Downtown Crossing", "Subway and Bus")
    South_Station = Station("South Station", "Subway and Bus")
    Broadway = Station("Broadway", "Subway and Bus")
    Andrew = Station("Andrew", "Subway and Bus")
    JFK_UMass = Station("JFK/UMass", "Subway and Bus")
    Government_Center = Station("Government Center", "Subway and Bus")
    Boylston = Station("Boylston", "Subway and Bus")
    Savin_Hill = Station("Savin Hill", "Subway")
    Fields_Corner = Station("Fields Corner", "Subway and Bus")
    Shawmut = Station("Shawmut", "Subway")
    Ashmont = Station("Ashmont", "Subway and Bus")
    North_Quincy = Station("North Quincy", "Subway and Bus")
    Wollaston = Station("Wollaston", "Subway")
    Quincy_Center = Station("Quincy Center", "Subway and Bus")
    Quincy_Adams = Station("Quincy Adams", "Subway and Bus")
    Braintree = Station("Braintree", "Subway and Bus")
    Arlington = Station("Arlington", "Subway and Bus")
    Copley = Station("Copley", "Subway and Bus")
    Hynes_Convention = Station("Hynes Convention Center", "Subway and Bus")
    Kenmore = Station("Kenmore", "Subway and Bus")
    Blandford = Station("Blandford Street", "Subway and Bus")
    Saint_Mary = Station("Saint Mary's Street", "Subway and Bus")
    Fenway = Station("Fenway", "Subway and Bus")
    Prudential = Station("Prudential", "Subway and Bus")
    Union_Square = Station("Union Square", "Subway and Bus")
    Lechmere = Station("Lechmere", "Subway and Bus")
    Science_Park = Station("Science Park/West End", "Subway and Bus")
    North_Station = Station("North Station", "Subway and Bus")
    Haymarket = Station("Haymarket", "Subway and Bus")
    Tufts = Station("Medford/Tufts", "Subway and Bus")
    Ball_Square = Station("Ball Square", "Subway and Bus")
    Magoun_Square = Station("Magoun Square", "Subway")
    Gilman_Square = Station("Gilman Square", "Subway and Bus")
    East_Som = Station("East Somerville", "Subway")


    Davis_Red = Subway("Davis", "Red Line")
    Porter_Red = Subway("Porter", "Red Line")
    Harvard_Red = Subway("Harvard", "Red Line")
    Kendall_Red = Subway("Kendall/MIT", "Red Line")
    Central_Red = Subway("Central", "Red Line")
    Charles_Red = Subway("Charles/MGH", "Red Line")
    Park_Street_Red = Subway("Park Street", "Red Line")
    Downtown_Red = Subway("Downtown Crossing", "Red Line")
    South_Station_Red = Subway("South Station", "Red Line")
    Broadway_Red = Subway("Broadway", "Red Line")
    Andrew_Red = Subway("Andrew", "Red Line")
    JFK_Red = Subway("JFK/UMass", "Red Line")
    Savin_Red = Subway("Savin Hill", "Red Line")
    Fields_Corner_Red = Subway("Fields Corner", "Red Line")
    Shawmut_Red = Subway("Shawmut", "Red Line")
    Ashmont_Red = Subway("Ashmont", "Red Line")
    North_Quincy_Red = Subway("North Quincy", "Red Line")
    Wollaston_Red = Subway("Wollaston", "Red Line")
    Quincy_Center_Red = Subway("Quincy Center", "Red Line")
    Quincy_Adams_Red = Subway("Quincy Adams", "Red Line")
    Braintree_Red = Subway("Braintree", "Red Line")

    Park_Street_B = Subway("Park Street", "Green Line -- any")
    Boylston_B = Subway("Boylston", "Green Line -- any")
    Arlington_B = Subway("Arlington", "Green Line -- any")
    Copley_B = Subway("Copley", "Green Line -- any")
    Hynes_B = Subway("Hynes Convention Center", "Green Line -- B, C, or D")
    Kenmore_B = Subway("Kenmore", "Green Line -- B, C, or D")
    Blandford_B = Subway("Blandford Street", "Green Line -- B")

    Park_Street_C = Subway("Park Street", "Green Line -- any")
    Boylston_C = Subway("Boylston", "Green Line -- any")
    Arlington_C = Subway("Arlington", "Green Line -- any")
    Copley_C = Subway("Arlington", "Green Line -- any")
    Hynes_C = Subway("Hynes Convention Center", "Green Line -- B, C, or D")
    Kenmore_C = Subway("Kenmore", "Green Line -- B, C, or D")
    Saint_Mary_C = Subway("Saint Mary's Street", "Green Line -- C")

    Union_Square_D = Subway("Union Square", "Green Line -- D")
    Lechmere_D = Subway("Lechmere", "Green Line -- D")
    Science_Park_D = Subway("Science Park/West End", "Green Line -- D")
    North_Station_D = Subway("North Station", "Green Line -- D")
    Haymarket_D = Subway("Haymarket", "Green Line -- D")
    Government_Center_D = Subway("Government Center", "Green Line -- any")
    Park_Street_D = Subway("Park Street", "Green Line -- any")
    Boylston_D = Subway("Boylston", "Green Line -- any")
    Arlington_D = Subway("Arlington", "Green Line -- any")
    Copley_D = Subway("Copley", "Green Line -- any")
    Hynes_D = Subway("Hynes Convention Center", "Green Line -- B, C, or D")
    Kenmore_D = Subway("Kenmore", "Green Line -- B, C, or D")
    Fenway_D = Subway("Fenway", "Green Line -- D")

    Medford_E = Subway("Medford/Tufts", "Green Line -- E")
    Ball_E = Subway("Ball Square", "Green Line -- E")
    Magoun_Square_E = Subway("Magoun Square", "Green Line -- E")
    Gilman_Square_E = Subway("Gilman Square", "Green Line -- E")
    East_Som_E = Subway("East Somerville", "Green Line -- E")
    Lechmere_E = Subway("Lechmere", "Green Line -- E")
    Science_Park_E = Subway("Science Park/West End", "Green Line -- E")
    North_Station_E = Subway("North Station", "Green Line -- E")
    Haymarket_E = Subway("Haymarket", "Green Line -- E")
    Government_Center_E = Subway("Government Center", "Green Line -- any")
    Park_Street_E = Subway("Park Street", "Green Line -- any")
    Boylston_E = Subway("Boylston", "Green Line -- any")
    Arlington_E = Subway("Arlington", "Green Line -- any")
    Copley_E = Subway("Copley", "Green Line -- any")
    Prudential_E = Subway("Prudential", "Green Line -- E")

    station_list = [Alewife, Davis, Porter, Harvard, Central, Kendall_MIT, Charles_MGH, Park_Street, Downtown_Crossing,
                    South_Station, Broadway, Andrew, JFK_UMass, Government_Center, Boylston, Savin_Hill, Fields_Corner, Shawmut,
                    Ashmont, North_Quincy, Wollaston, Quincy_Center, Quincy_Adams, Braintree, Arlington, Copley, Hynes_Convention,
                    Kenmore, Blandford, Saint_Mary, Fenway, Prudential, Union_Square, Lechmere, Science_Park, North_Station,
                    Haymarket, Tufts, Ball_Square, Magoun_Square, Gilman_Square, East_Som]

    station_graph = {Alewife : [Davis_Red],
                     Davis : [Porter_Red],
                     Porter : [Harvard_Red],
                     Harvard : [Central_Red],
                     Central : [Kendall_Red],
                     Kendall_MIT : [Charles_Red],
                     Charles_MGH : [Park_Street_Red],
                     Park_Street : [Downtown_Red, Boylston_B, Boylston_C, Boylston_D, Boylston_E],
                     Downtown_Crossing : [South_Station_Red],
                     South_Station : [Broadway_Red],
                     Broadway : [Andrew_Red],
                     Andrew : [JFK_Red],
                     JFK_UMass : [Savin_Red, North_Quincy_Red],
                     Savin_Hill : [Fields_Corner_Red],
                     Fields_Corner : [Shawmut_Red],
                     Shawmut : [Ashmont_Red],
                     Ashmont : [],
                     North_Quincy : [Wollaston_Red],
                     Wollaston : [Quincy_Center_Red],
                     Quincy_Center : [Quincy_Adams_Red],
                     Quincy_Adams : [Braintree_Red],
                     Braintree : [],
                     Government_Center : [Park_Street_B, Park_Street_C, Park_Street_D, Park_Street_E],
                     Boylston : [Arlington_B, Arlington_C, Arlington_D, Arlington_E],
                     Arlington : [Copley_B, Copley_C, Copley_D, Copley_E],
                     Copley : [Hynes_B, Hynes_C, Hynes_D, Prudential_E],
                     Prudential : [],
                     Hynes_Convention : [Kenmore_B, Kenmore_C, Kenmore_D],
                     Kenmore : [Blandford_B, Saint_Mary_C, Fenway_D],
                     Blandford : [],
                     Saint_Mary : [],
                     Fenway : [],
                     }
    
    ride_map(station_graph, station_list, Central, Prudential, [])
    

def ride_map(stat_graph, stat_list, start, end, path):

    explored = []

    queue = [[start]]

    line_list = []

    station_counts = defaultdict(int)

    if start.name == end.name:
        print("You are already at your intended destination.")
        return queue
    
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            
            if type(node) != Station:
                curr_route = node.route
                curr_name = node.name
                line_list.append((curr_name, curr_route))
                for station in stat_list:
                    if station.name == node.name:
                        node = station

            neighbors = stat_graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor.name == end.name:
                    line_list.append((neighbor.name, neighbor.route))
                    names_path = []
                    for stop in new_path:
                        names_path.append(stop.name)
                        
                    route = line_list[0][1]
                    print(">>", route)
                    
                    station_counts = defaultdict(int)

                    updated_line_list = []
                    for line in line_list:
                        if line[0] in names_path and station_counts[line[0]] == 0:
                            updated_line_list.append(line)
                            station_counts[line[0]] += 1

                    j = 0
                    for station in new_path:
                        if j < len(updated_line_list):
                            if updated_line_list[j][0] in names_path:
                                if updated_line_list[j][1] != route:
                                    print(">>", updated_line_list[j][1])
                                    route = updated_line_list[j][1]
                        print(station.name)
                        j += 1
                    return new_path
                
            explored.append(node)
    
    return None


            
main()


