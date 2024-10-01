from TrainTypes import Subway
from TrainTypes import Station

def main():

    Alewife = Station("Alewife", "Subway and Bus")
    Davis = Station("Davis", "Subway and Bus")
    Davis_Red = Subway("Davis")
    Porter = Station("Porter", "Subway and Bus")
    Porter_Red = Subway("Porter")
    Harvard_Red = Subway("Harvard")
    Central = Station("Central", "Subway and Bus")
    Harvard = Station("Harvard", "Subway and Bus")
    Kendall_MIT = Station("Kendall/MIT", "Subway and Bus")
    Charles_MGH = Station("Charles/MGH", "Subway")
    Park_Street = Station("Park_Street", "Subway and Bus")
    Downtown_Crossing = Station("Downtown Crossing", "Subway and Bus")
    South_Station = Station("South Station", "Subway and Bus")
    Broadway = Station("Broadway", "Subway and Bus")
    Andrew = Station("Andrew", "Subway and Bus")
    JFK_UMass = Station("JFK/UMass", "Subway and Bus")
    
    Government_Center = Station("Government Center", "Subway and Bus")
    Boylston = Station("Boylston", "Subway and Bus")

    station_list = [Alewife, Davis, Porter, Harvard]

    station_graph = {Alewife : [Davis_Red],
                     Davis : [Porter_Red],
                     Porter : [Harvard_Red],
                     Harvard : []
                    #  Harvard: [Central],
                    #  Central : [Kendall_MIT],
                    #  Kendall_MIT : [Charles_MGH],
                    #  Charles_MGH : [Park_Street],
                    #  Park_Street : [Downtown_Crossing],
                    #  Downtown_Crossing : [South_Station],
                    #  South_Station : [Broadway],
                    #  Broadway : [Andrew],
                    #  Andrew : [JFK_UMass],
                    #  JFK_UMass : []
                     }
    
    ride_map(station_graph, station_list, Alewife, Harvard, [])
    

def ride_map(stat_graph, stat_list, start, end, path):

    explored = []

    queue = [[start]]

    if start.name == end.name:
        print("You are already at your intended destination.")
        return queue
    
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            if type(node) != Station:
                for station in stat_list:
                    if station.name == node.name:
                        node = station
            neighbors = stat_graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor.name == end.name:
                    for station in new_path:
                        print(station.name)
                    return new_path
            explored.append(node)
    
    return None


            
main()


