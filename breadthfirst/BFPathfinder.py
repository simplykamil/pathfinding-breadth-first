from mazecreator.Creator import Creator


class BFPathfinder:
    @staticmethod
    def find_path():
        GRID = Creator.get_grid()

        [print(x) for x in GRID]


if __name__ == '__main__':
    BFPathfinder.find_path()
