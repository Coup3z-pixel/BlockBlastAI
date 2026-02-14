import math
import random

from game.Block import Block


class BlockBlast:
    def __init__(self, row=8, column=8):
        self.state = [[False for _ in range(row)] for _ in range(column)]

        self.points = 0

        self.blocks = [None, None, None]
        self.used_blocks = [False, False, False]

        self.generate_blocks()

        self.row_size = row
        self.col_size = column

    def generate_blocks(self) -> list[Block]:
        block_ids = [random.randint(1, 10) for _ in range(3)]
        self.blocks = [Block(block_id) for block_id in block_ids]
        self.used_blocks = [False for _ in range(3)]

        return self.blocks

    def place(self, row: int, col: int, index: int):
        if self.used_blocks[index]:
            raise Exception("block already used")

        self.__place_block(row, col, index)

        self.used_blocks[index] = True

        points_gained = self.__update_game_and_points()

        self.points += points_gained

        if False not in self.used_blocks:
            self.generate_blocks()

        return points_gained

    def __can_block_be_placed(
        self, placement_row: int, placement_col: int, block_index: int
    ):
        for r, row in enumerate(self.blocks[block_index].block):
            for c, col in enumerate(row):
                if not col:
                    continue

                if (
                    placement_row + r >= self.row_size
                    or placement_col + c >= self.col_size
                ) or (self.state[placement_row + r][placement_col + c] and col):
                    return False

        return True

    def __place_block(self, placement_row: int, placement_col: int, index: int):
        if not self.__can_block_be_placed(placement_row, placement_col, index):
            raise Exception("can't place block there")

        for r, row in enumerate(self.blocks[index].block):
            for c, col in enumerate(row):
                if not col:
                    continue

                self.state[placement_row + r][placement_col + c] = col

    def __update_game_and_points(self) -> int:

        rows_to_remove = [False for _ in range(self.row_size)]
        cols_to_remove = [False for _ in range(self.col_size)]

        for r, row in enumerate(self.state):
            if not False in row:
                rows_to_remove[r] = True

        for c in range(len(self.state[0])):
            all_occupied = True

            for r in range(len(self.state)):
                if not self.state[r][c]:
                    all_occupied = False
                    break

            if all_occupied:
                cols_to_remove[c] = True

        removed_lines = 0

        for r, remove_row in enumerate(rows_to_remove):
            if remove_row:
                for c in range(len(self.state[0])):
                    self.state[r][c] = False

                removed_lines += 1

        for c, remove_col in enumerate(cols_to_remove):
            if remove_col:
                for r in range(len(self.state)):
                    self.state[r][c] = False

                removed_lines += 1

        return math.exp(0.4 * removed_lines)

    def is_playable(self) -> bool:
        for blockIndex in range(0, len(self.blocks)):
            for r in range(0, len(self.state)):
                for c in range(0, len(self.state[0])):
                    if self.__can_block_be_placed(r, c, blockIndex):
                        return True

        return False

    def __str__(self):
        res = ""

        for row in self.state:
            for col in row:
                res += str(1 if col else 0)

            res += "\n"

        return res
