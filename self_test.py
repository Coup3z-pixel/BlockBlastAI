import os

from game.BlockBlast import BlockBlast


def manual_test():
    game = BlockBlast(8, 8)

    while True:
        print(game)

        blocks = game.blocks if False in game.used_blocks else game.generate_blocks()

        for index, block in enumerate(blocks):
            print(f"Block {index+1}: ")

            if not game.used_blocks[index]:
                print(block)
            else:
                print("ALREADY USED \n" * 5)

        block_index = int(input("Block: ")) - 1
        col_index = int(input("Column: "))
        row_index = int(input("Row: "))

        try:
            while False in game.used_blocks:
                game.place(row_index, col_index, block_index)
        except Exception as e:
            print(e)

        if not game.is_playable():
            break


if __name__ == "__main__":
    manual_test()
