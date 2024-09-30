from TrainTypes import Subway
from TrainTypes import Station

def main():

    Alewife = Station("Alewife", "Red Line")
    Davis = Station("Davis", "Subway")
    West_Service_Rd_Lake_St = Station("West Service Rd @ Lake St", "Bus")
    Mass_Route_16 = Station("Massachusetts Ave @ Rt 16", "Bus")
    Grove_St_Highland = Station("Grove St @ Highland Ave", "Bus")
    Holland_St_Simpson = Station("Holland St @ Simpson Ave", "Bus")
    College_Ave_Francesca = Station("College Ave @ Francesca Ave", "Bus")
    Porter = Station("Porter", "Red Line")
    Central = Station("Central", "Red Line")
    Harvard = Station("Harvard", "Red Line")
    West_Service_Venner = Station("West Service Rd @ Venner Rd", "Bus")
    Pleasant_Opp_Brunswick = Station("West Service Rd @ Venner Rd", "Bus")

    station_graph = {Alewife : [Davis],
                     Davis : [Porter],
                     Porter : [Harvard],
                     Harvard: [Central],
                     Central : []
                     }
    
    ride_map(station_graph, Alewife, Harvard, [])
    

def ride_map(graph, start, end, path):
    path = path + [start]
    if start == end:
        for path in path:
            print(path.name)
        return path
    if not start in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = ride_map(graph, node, end, path)
            if newpath: return newpath
    
    return None


            
main()


