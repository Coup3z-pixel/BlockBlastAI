import random

from game.BlockBlast import BlockBlast


class Environment:
    """docstring for Environment."""

    def __init__(self):
        self.curr_game = None
        self.action_space = None

    def get_curr_state(self):
        one_dimensional_state = []

        for row in self.curr_game.state:
            one_dimensional_state += row

        for block_i, block in enumerate(self.curr_game.blocks):
            if not self.curr_game.used_blocks[block_i]:
                one_dimensional_state += [-1, -1, -1, -1, -1] * 5
                continue

            for row in block.block:
                one_dimensional_state += row

        state_as_ints = [1 if cell else 0 for cell in one_dimensional_state]

        return state_as_ints

    def reset(
        self,
    ) -> [list[list[bool]], list[list[bool]], list[list[bool]], list[list[bool]]]:
        self.curr_game = BlockBlast()

        return self.get_curr_state()

    def step(self, action_item) -> (list[int], int, bool, bool, int):

        block = action_item // 64
        cell = action_item % 64
        r = cell // 8
        c = cell % 8

        reward = 0

        try:
            reward = self.curr_game.place(r, c, block)
        except Exception as e:
            print(e)
            reward = -10

        return (
            self.get_curr_state(),
            reward,
            not self.curr_game.is_playable(),
        )

    def sample(self):
        available = []

        for block_i, block_used in enumerate(self.curr_game.used_blocks):
            if not block_used:
                available.append(block_i)

        chosen_block = random.choice(available)

        return chosen_block * 64 + random.randint(0, 63)

    def curr_game_playable(self) -> bool:
        return self.curr_game.is_playable()
