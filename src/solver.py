#!/bin/bash/python3
from copy import deepcopy
import heapq
import Parser
import time
from decimal import *

recursion_depth=20

class Puzzle:
    # current board state
    board = []
    # board width
    width = 0
    # board height
    height = 0
    # recursion depth of given state
    depth = 0
    # path to starting state
    path = []
    # last move
    lastMove = ''
    # distance for astr
    distance = 0

    def __init__(self, arg):
        # create state from file
        if isinstance(arg, str):
            with open(arg) as f:
                self.height, self.width = [int(x) for x in next(f).split()]
                for line in f:
                    self.board.append([int(x) for x in line.split()])
        # create state from higher state, depth increment by one
        elif isinstance(arg, Puzzle):
            self.board = deepcopy(arg.board)
            self.width = deepcopy(arg.width)
            self.height = deepcopy(arg.height)
            self.path = deepcopy(arg.path)
            self.lastMove = deepcopy(arg.lastMove)
            self.depth = deepcopy(arg.depth)+1
        else:
            raise TypeError("Argument is neither path nor puzzle!")

    def __eq__(self, other):
        return self.distance == other.distance

    def __ne__(self, other):
        return self.distance != other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __str__(self):
        return str(self.board)

    def __hash__(self):
        return hash(str(self))

    def get_zero_pos(self):
        # get position of zero in given state
        for h in range(self.height):
            for w in range(self.width):
                if self.board[h][w] == 0:
                    return h, w

    def swap(self, h1, w1, h2, w2):
        # swaps two tiles in current state
        temp = self.board[h1][w1]
        self.board[h1][w1] = self.board[h2][w2]
        self.board[h2][w2] = temp

    def get_possible_moves(self):
        # gets list of possible moves for zero
        h, w = self.get_zero_pos()
        ret = []
        if h != self.height-1:
            ret.append('D')
        if h != 0:
            ret.append('U')
        if w != self.width-1:
            ret.append('R')
        if w != 0:
            ret.append('L')
        return ret

    def move_zero_tile(self, priority):
        # moves zero in bfs and dfs cases, returns opposite moves for further utility
        h0, w0 = self.get_zero_pos()
        if priority == 'U':
            self.swap(h0, w0, h0 - 1, w0)
            self.lastMove = 'D'
            return 'U'
        elif priority == 'D':
            self.swap(h0, w0, h0 + 1, w0)
            self.lastMove = 'U'
            return 'D'
        elif priority == 'L':
            self.swap(h0, w0, h0, w0 - 1)
            self.lastMove = 'R'
            return 'L'
        else:
            self.swap(h0, w0, h0, w0 + 1)
            self.lastMove = 'L'
            return 'R'

    def is_goal_state(self):
        # checks if state is goal state
        if self.board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
            return True
        return False

    def generate_new_states(self, priority):
        # generates states in bfs and dfs cases, return list of states
        kids = []
        for i in range(4):
            # generate states with priority                 # that's why move_zero_tile returns opposite moves
            if priority[i] in self.get_possible_moves() and priority[i] != self.lastMove:
                new = Puzzle(self)
                new.path.append(new.move_zero_tile(priority[i]))
                kids.append(new)
        return kids

    def solve_bfs(self, priority, recursion_depth):
        # solves puzzle with breadth-first-sarch
        start_state = Puzzle(self)
        visited = 0
        frontier = [start_state]
        exfrontier = set()
        recursion = 1
        processed = 0
        while len(frontier) > 0:
            processed += 1
            state = frontier.pop(0)
            if state.depth > recursion:
                recursion = state.depth
            if state.is_goal_state():
                return len(state.path), state.path, visited, processed, recursion
            if state.depth < recursion_depth:
                x = state.generate_new_states(priority)
                for i in x:
                    if i in exfrontier:
                        x.remove(i)
                    if i.is_goal_state():
                        return len(i.path), i.path, visited, processed, recursion
                    exfrontier.add(i)
                    visited += 1
                frontier.extend(x)
        return -1, [], visited, processed, recursion

    def solve_dfs(self, priority, recursion_depth):
        # solves puzzle with depth-first-search
        start_state = Puzzle(self)
        visited = 0
        frontier = [start_state]
        exfrontier = set()
        recursion = 0
        processed = 0
        while len(frontier) > 0:
            processed += 1
            state = frontier.pop(0)
            if state.depth > recursion:
                recursion = state.depth
            if state.depth < recursion_depth:
                x = state.generate_new_states(priority)
                for i in x:
                    if i in exfrontier:
                        x.remove(i)
                    if i.is_goal_state():
                        return len(i.path), i.path, visited, processed, recursion
                    visited += 1
                    exfrontier.add(i)
                frontier = x + frontier
        return -1, [], visited, processed, recursion

    def hamming_metric(self):
        misplaced = 0
        for h in range(self.height):
            for w in range(self.width):
                if h==self.height-1 and w==self.width-1:
                    if self.board[h][w] != 0:
                        misplaced += 1
                elif self.board[h][w] != self.width*h+w+1:
                    misplaced += 1
        self.distance = misplaced

    def manhattan_metric(self):
        distance = 0
        for h in range(self.height):
            for w in range(self.width):
                x = self.board[h][w]
                if x == 0:
                    pass
                distance += abs(h-int((x-1)/self.width)) + abs(w-((x-1)%self.width))
        self.distance = distance

    def solve_astr(self, metric, recursion_depth):
        states = []
        visited = 0
        recursion = 0
        processed = 0
        priority = ['U', 'L', 'D', 'R']
        heapq.heappush(states, self)
        while len(states) > 0:
            processed += 1
            state = heapq.heappop(states)
            if state.depth < recursion_depth:
                x = state.generate_new_states(priority)
                for i in x:
                    if i.depth > recursion:
                        recursion = i.depth
                    if i.is_goal_state():
                        return len(i.path), i.path, visited, processed, recursion
                    if metric == "hamm":
                        i.hamming_metric()
                    else:
                        i.manhattan_metric()
                    visited += 1
                    heapq.heappush(states, i)
        return -1, [], visited, processed, recursion


if __name__ == "__main__":
    P = Parser.Parser()
    P.parse()
    input_path = P.get_input()
    solution = P.get_solution()
    more = P.get_stats()
    priority = P.get_priority()
    algorithm = P.get_algorithm()

    p1 = Puzzle(input_path)

    if algorithm == 'bfs':
        priority1 = []
        for p in priority:
            priority1.append(p)
        start_time = time.time()
        amount, path, visited, processed, recursed = p1.solve_bfs(priority1, recursion_depth)
        time = time.time() - start_time
    elif algorithm == 'dfs':
        priority1 = []
        for p in priority:
            priority1.append(p)
        start_time = time.time()
        amount, path, visited, processed, recursed = p1.solve_dfs(priority1, recursion_depth)
        time = time.time() - start_time
    elif algorithm == 'astr':
        start_time = time.time()
        amount, path, visited, processed, recursed = p1.solve_astr(priority, recursion_depth)
        time = time.time() - start_time

    f = open(solution, 'x')
    f.close()

    f = open(solution, 'a')
    f.write(str(amount)+"\n")
    if amount != -1:
        f.write("".join(path)+"\n")
    f.close()

    f = open(more, 'x')
    f.close()

    f = open(more, 'a')
    f.write(str(amount)+"\n")
    f.write(str(visited)+"\n")
    f.write(str(processed)+"\n")
    f.write(str(recursed)+"\n")
    f.write(str(round(time,3)))
    f.close()
