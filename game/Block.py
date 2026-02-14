class Block:
    def __init__(self, block_id: int):
        match block_id:
            case 1:
                self.block = [
                    [True, True, True, True, True],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 2:
                self.block = [
                    [True, False, False, False, False],
                    [True, False, False, False, False],
                    [True, False, False, False, False],
                    [True, False, False, False, False],
                    [True, False, False, False, False],
                ]
            case 3:
                self.block = [
                    [True, True, True, False, False],
                    [True, True, True, False, False],
                    [True, True, True, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 4:
                self.block = [
                    [True, True, True, False, False],
                    [True, True, True, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 5:
                self.block = [
                    [True, True, False, False, False],
                    [True, True, False, False, False],
                    [True, True, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 6:
                self.block = [
                    [True, True, True, False, False],
                    [True, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 7:
                self.block = [
                    [True, True, False, False, False],
                    [True, False, False, False, False],
                    [True, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 8:
                self.block = [
                    [True, True, True, False, False],
                    [False, True, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 9:
                self.block = [
                    [True, False, False, False, False],
                    [True, True, False, False, False],
                    [True, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case 10:
                self.block = [
                    [True, True, False, False, False],
                    [True, True, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                ]
            case _:
                raise Exception("Block id doesn't exist")

    def __str__(self):
        res = ""

        for row in self.block:
            for col in row:
                res += str(1 if col else 0)

            res += "\n"

        return res
