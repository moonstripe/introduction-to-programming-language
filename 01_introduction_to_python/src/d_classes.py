class Building:
    def __init__(self, address: str, max_occupancy: int):
        self.address = address
        self.max_occupancy = max_occupancy

        self.unit_map: dict = {}

        for unit in range(self.max_occupancy):
            self.unit_map[str(unit)] = None
    
    def fill_vacancy(self, name: str) -> str:
        for unit in self.unit_map:
            if self.unit_map[unit] is None:
                self.unit_map[unit] = name

                print(f'Welcome to unit {unit}, {name}!')
                return unit
        
        raise Exception(f'No units found for {name}...')

if __name__ == "__main__":
    # hey, if this script is called DIRECTLY (python3 ...../d_classes.py)
    # run the following code
    new_dorm = Building('460 Pierce St', 8)

    print(f'new_dorm address: {new_dorm.address}')

    print(f'new_dorm maximum occupancy: {new_dorm.max_occupancy}')

    print(f'new_dorm unit map: {new_dorm.unit_map}')

    students = ['kojin', 'steve', 'cathy', 'nicole', 'pablo', 'artem', 'cyril', 'cassandra', 'paul']

    for student in students:
        new_dorm.fill_vacancy(student)
        print(f'Dorm Unit Map: {new_dorm.unit_map}')