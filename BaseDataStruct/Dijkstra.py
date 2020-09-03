class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_routes(self,city, price_info):
        self.routes[city] = price_info

def dijikstra(starting_city, other_cities):
    routes_from_city = {}
    routes_from_city[starting_city] = [0, starting_city]
    for city in other_cities:
        routes_from_city[city] = [float('inf'), None]
    # 已经访问的城市记录在这个数组中
    visited_cities = []
    current_city = starting_city
    while current_city:
        visited_cities.append(current_city)
        for city, price_info in current_city.routes.items():
            if routes_from_city[city][0] > price_info + routes_from_city[current_city][0]:
                routes_from_city[city] = [price_info + routes_from_city[current_city][0], current_city]

        #
        current_city = None
        cheapest_route_from_current_city = float('inf')
        for city, price_info in routes_from_city.items():
            if price_info[0] < cheapest_route_from_current_city and city not in visited_cities:
                cheapest_route_from_current_city = price_info[0]
                current_city = city

    return routes_from_city
if __name__ == '__main__':
    atlanta = City("Atlanta")
    boston = City("Boston")
    chicago = City("Chicago")
    denver = City("Denver")
    el_paso = City("El Paso")

    atlanta.add_routes(boston, 100)
    atlanta.add_routes(denver, 160)
    boston.add_routes(chicago, 120)
    boston.add_routes(denver, 180)
    chicago.add_routes(el_paso, 80)
    denver.add_routes(chicago, 40)
    denver.add_routes(el_paso, 140)

    routes = dijikstra(atlanta, [boston, chicago, denver, el_paso])
    for city, price_info in routes.items():
        print(str(city.name) + "->" + str(price_info[0]))
