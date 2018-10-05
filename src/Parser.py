import argparse


class Parser:

    def __init__(self):

        self._parser = argparse.ArgumentParser(description='15 Puzzle solver')

        self._parser.add_argument('-a', '--algorithm', choices=['bfs', 'dfs', 'manh', 'hamm'], required=True, type=str,
                                  help='Choose which algorithm to use\nbfs - breadth-first-search\ndfs - '
                                       'depth-first-serach\nmanh - A* search with manhattan metric\nhamm - A* '
                                       'algorithm with Hamming metric')

        self._parser.add_argument('-i', '--input', type=str, required=True,
                                  help='Specify path for input file')

        self._parser.add_argument('-s', '--solution', type=str, required=True,
                                  help='Specify path for solution file')

        self._parser.add_argument('-m', '--more_info', required=True, type=str,
                                  help='Specify path for more info file')

        self._parser.add_argument('-r', '--recursion_depth', type=int, default=20,
                                  help='Specify maximum depth of recursion')

        self._parser.add_argument('-p', '--priority', choices=['U', 'D', 'L', 'R'], nargs=4, default=['U', 'L', 'D', 'R'],
                                  help='Specify priority of blank tile moves separated by spaces')

    def parse(self):
        self._args = self._parser.parse_args()

    def get_algorithm(self):
        return self._args.algorithm

    def get_input(self):
        return self._args.input

    def get_solution(self):
        return self._args.solution

    def get_more_info(self):
        return self._args.more_info

    def get_recursion_depth(self):
        return self._args.recursion_depth

    def get_priority(self):
        return self._args.priority
