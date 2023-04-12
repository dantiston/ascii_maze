#!/usr/bin/env python3

from collections import deque
from pprint import pprint
from typing import Iterable, Literal


END_TILE = "E"
OPEN_TILE = " "
PLAYER_TILE = "@"
START_TILE = "S"
WALL_TILE = "#"

Tile = Literal[" ", "@", "#", "S", "E"]
Maze = list[list[Tile]]
Position = tuple[int, int]
Path = list[Position]


def _get_position_for_tile(maze: Maze, tile: Tile) -> Position | None:
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == tile:
                return i, j
    return None


def _set_cursor(maze: Maze, position: Position) -> Maze:
    result = [list(row) for row in maze]
    y, x = position
    result[y][x] = "@"
    return result


def _valid_moves(maze: Maze, position: Position) -> Iterable[Position]:
    y, x = position
    valid_moves = {END_TILE, OPEN_TILE}
    if y + 1 < len(maze) and maze[y + 1][x] in valid_moves:
        yield y + 1, x
    if y - 1 >= 0 and maze[y - 1][x] in valid_moves:
        yield y - 1, x
    if x + 1 < len(maze[y]) and maze[y][x + 1] in valid_moves:
        yield y, x + 1
    if x - 1 >= 0 and maze[y][x - 1] in valid_moves:
        yield y, x - 1


def is_solvable(maze: Maze) -> bool:
    end = _get_position_for_tile(maze, END_TILE)
    if end:
        path = list(get_path(maze))
        if path:
            final_position = path[-1][0]
            if final_position == end:
                return True
    return False


def get_path(maze: Maze) -> Iterable[tuple[Position, Maze]]:
    start: Position = _get_position_for_tile(maze, START_TILE)
    if not start:
        return None
    queue: deque[Position] = deque([start])
    visited = set()
    while queue:
        current = queue.popleft()
        yield current, _set_cursor(maze, current)
        y, x = current
        if maze[y][x] == END_TILE:
            return None
        visited.add(current)
        queue.extend(set(_valid_moves(maze, current)) - visited)



moves = {
    ".": (1, 0),
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    # "\x1b[A": (-1, 0),
    # "\x1b[B": (1, 0),
    # "\x1b[C": (0, 1),
    # "\x1b[D": (0, -1),
}

def interactive_search(maze: Maze) -> None:
    solved = False
    current_position: Position = _get_position_for_tile(sample, START_TILE)
    current = [list(row) for row in sample]
    while not solved:
        pprint(current)
        next_move = input("{<^>.}> ").strip()
        if next_move not in moves:
            continue
        offset = moves[next_move]
        y, x = tuple(sum(pair) for pair in zip(*(current_position, offset)))
        if y >= 0 and y < len(sample) and x >= 0 and x < len(sample[y]):
            next_tile = sample[y][x]
            if next_tile in {END_TILE, OPEN_TILE}:
                current_position = y, x
                current = _set_cursor(sample, current_position)
                if next_tile == END_TILE:
                    print("*"*80)
                    print("*"*35, "Success!", "*"*35)
                    print("*"*80)
                    solved = True



if __name__ == "__main__":
    sample = [
        ["S", " ", "*", "*", "*"],
        ["*", " ", " ", "*", "*"],
        ["*", "*", " ", "*", "*"],
        ["*", "*", " ", " ", "*"],
        ["*", "*", "*", " ", "E"],
    ]
    interactive_search(sample)
