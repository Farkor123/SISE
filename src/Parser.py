import argparse


class Parser:

    def __init__(self):

        self._parser = argparse.ArgumentParser(description='15 Puzzle solver')

        self._parser.add_argument('algorithm', type=str,
                                  help='Choose which algorithm to use\nbfs - breadth-first-search\ndfs - '
                                       'depth-first-serach\nmanh - A* search with manhattan metric\nhamm - A* '
                                       'algorithm with Hamming metric')

        self._parser.add_argument('priority', type=str,
                                  help='Specify priority of blank tile moves separated by spaces')

        self._parser.add_argument('input', type=str,
                                  help='Specify path for input file')

        self._parser.add_argument('solution', type=str,
                                  help='Specify path for solution file')

        self._parser.add_argument('stats', type=str,
                                  help='Specify path for more info file')


    def parse(self):
        self._args = self._parser.parse_args()

    def get_algorithm(self):
        return self._args.algorithm

    def get_input(self):
        return self._args.input

    def get_solution(self):
        return self._args.solution

    def get_stats(self):
        return self._args.stats

    def get_priority(self):
        return self._args.priority
