def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    coordinates = []
    result = []
    for i in range(rows):
        for j in range(cols):
            coordinates.append([i,j])
    coord_dict = {}
    for point in coordinates:
        distance = abs(rCenter - point[0]) + abs(cCenter - point[1])
        if distance not in coord_dict.keys():
            coord_dict[distance] = [point]
        else:
            coord_dict[distance].append(point)
    
    for key in sorted(list(coord_dict.keys())):
        result += coord_dict[key]
    return result