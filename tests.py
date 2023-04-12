#!/usr/bin/env python3

import maze_utils
import pytest


@pytest.mark.parametrize(
    "maze,expected",
    [
        # base right; positive
        (
            [
                ["S", "E"],
            ],
            True,
        ),
        # base down; positive
        (
            [
                ["S"],
                ["E"],
            ],
            True,
        ),
        # base left; positive
        (
            [
                ["E", "S"],
            ],
            True,
        ),
        # base up; positive
        (
            [
                ["E"],
                ["S"],
            ],
            True,
        ),
        # base right; negative
        (
            [
                ["S", "*", "E"],
            ],
            False,
        ),
        # base down; negative
        (
            [
                ["S"],
                ["*"],
                ["E"],
            ],
            False,
        ),
        # base left; negative
        (
            [
                ["E", "*", "S"],
            ],
            False,
        ),
        # base up; negative
        (
            [
                ["E"],
                ["*"],
                ["S"],
            ],
            False,
        ),
        # missing end; negative
        (
            [
                ["S"],
            ],
            False,
        ),
        # missing end, blocked; negative
        (
            [
                ["S", "*"],
            ],
            False,
        ),
        # missing end, open; negative
        (
            [
                ["S", " "],
            ],
            False,
        ),
        # missing start
        (
            [
                [" ", "E"],
            ],
            False,
        ),
        # missing both
        (
            [
                [" "],
            ],
            False,
        ),
        # no valid locations
        (
            [
                [" "],
            ],
            False,
        ),
        # empty
        (
            [
                [],
            ],
            False,
        ),
        # base infinite
        (
            [
                ["S", " ", " ", "*", "E"],
            ],
            False,
        ),
    ],
)
def test_is_solvable(maze, expected):
    assert maze_utils.is_solvable(maze) == expected


@pytest.mark.parametrize(
    "maze,expected",
    [
        # base right
        (
            [
                ["S", "E"],
            ],
            [((0, 0), [["@", "E"]]), ((0, 1), [["S", "@"]])],
        ),
        # base down
        (
            [
                ["S"],
                ["E"],
            ],
            [
                (
                    (0, 0),
                    [
                        ["@"],
                        ["E"],
                    ],
                ),
                (
                    (1, 0),
                    [
                        ["S"],
                        ["@"],
                    ],
                ),
            ],
        ),
        # base left
        (
            [
                ["E", "S"],
            ],
            [((0, 1), [["E", "@"]]), ((0, 0), [["@", "S"]])],
        ),
        # base up
        (
            [
                ["E"],
                ["S"],
            ],
            [
                (
                    (1, 0),
                    [
                        ["E"],
                        ["@"],
                    ],
                ),
                (
                    (0, 0),
                    [
                        ["@"],
                        ["S"],
                    ],
                ),
            ],
        ),
        # base infinite
        (
            [
                ["S", " ", " ", "*", "E"],
            ],
            [
                (
                    (0, 0),
                    [
                        ["@", " ", " ", "*", "E"],
                    ],
                ),
                (
                    (0, 1),
                    [
                        ["S", "@", " ", "*", "E"],
                    ],
                ),
                (
                    (0, 2),
                    [
                        ["S", " ", "@", "*", "E"],
                    ],
                ),
            ],
        ),
    ],
)
def test_get_path(maze, expected):
    assert list(maze_utils.get_path(maze)) == expected
