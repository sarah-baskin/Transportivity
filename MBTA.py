from TrainTypes import Subway
from TrainTypes import Station

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

    Park_Street_Green = Subway("Park Street", "Green Line")
    Boylston_Green = Subway("Boylston", "Green Line")

    station_list = [Alewife, Davis, Porter, Harvard, Central, Charles_MGH, Park_Street, Downtown_Crossing,
                    South_Station, Broadway, Andrew, JFK_UMass, Government_Center, Boylston]

    station_graph = {Alewife : [Davis_Red],
                     Davis : [Porter_Red],
                     Porter : [Harvard_Red],
                     Harvard : [Central_Red],
                     Central : [Kendall_MIT],
                     Kendall_MIT : [Charles_Red],
                     Charles_MGH : [Park_Street_Red],
                     Park_Street : [Downtown_Red, Boylston_Green],
                     Downtown_Crossing : [South_Station_Red],
                     South_Station : [Broadway_Red],
                     Broadway : [Andrew_Red],
                     Andrew : [JFK_Red],
                     JFK_UMass : [],
                     Government_Center : [Park_Street_Green],
                     Boylston : []
                     }
    
    ride_map(station_graph, station_list, Government_Center, South_Station, [])
    

def ride_map(stat_graph, stat_list, start, end, path):

    explored = []

    queue = [[start]]

    line_list = []

    if start.name == end.name:
        print("You are already at your intended destination.")
        return queue
    
    i = 0
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            if type(node) != Station:
                line_list.append((node.route, i))
                i += 1
                for station in stat_list:
                    if station.name == node.name:
                        node = station
            neighbors = stat_graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor.name == end.name:
                    route = line_list[0][0]
                    print(">>", route)
                    j = 1
                    for station in new_path:
                        print(station.name)
                        if line_list[j][0] != route:
                            print(">>", line_list[j][0])
                            route = line_list[j][0]
                    return new_path
            explored.append(node)
    
    return None


            
main()


