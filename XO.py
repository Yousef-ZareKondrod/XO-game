from typing import Literal, Union, Optional


class _Player:
    def __init__(self, name: str, sign: Literal['x', 'o']) -> None:
        self.name = name
        self.sign = sign


class _XOTable:
    xo_map = {k: None for k in range(1, 10)}  # {1:x, 2: None, 3: o, ...}

    def __str__(self):
        map = self.xo_map
        return """
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
""".format(*[map[i] if map[i] else i for i in map])

    def mark(self, cell_no, sign: str):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Enter a valid cell no [1, 9]"
        assert not self.xo_map[cell_no], "Cell is filled"
        sign = str(sign).lower()
        assert sign in 'xo', 'Invalid sign' + sign
        self.xo_map[cell_no] = sign


class _XOGame(_XOTable):
    class UnFinishedGameError(Exception):
        "winner: zamani raise mishe k, bazi tamoom nashode bahe, vali winner() ..."
        pass

    class FinishedGameError(Exception):
        "mark: dar zamin k bazi tamoom shde ..."
        pass

    class InvalidCellError(Exception):
        "mark: Che por bashe, che addesh eshtabah bashe va ..."
        pass

    class Wrong_Cell_Number(InvalidCellError):
        cell_no: int

        def __init__(self, cell_no, *args):
            super().__init__(*args)
            self.cell_no = cell_no

    class InvalidPlayer(Exception):
        "mark: palyere voroodi eshtebah bashad!!!"
        pass

    def __init__(self, player1: _Player, player2: _Player) -> None:
        self.player1 = player1
        self.player2 = player2

    def _calculate_result(self):
        t = _XOTable()
        print(t)
        winner_player: str
        for i in range(3):
            if self.xo_map[i * 3 + 1] == self.xo_map[i * 3 + 2] == self.xo_map[i * 3 + 3] and\
                    isinstance(self.xo_map[i * 3 + 1], str):
                return self.xo_map[i * 3 + 1]
            if self.xo_map[(i + 1)] == self.xo_map[(i + 1) + 3] == self.xo_map[(i + 1) + 6] and\
                    isinstance(self.xo_map[(i + 1)], str):
                return self.xo_map[i + 1]
        if self.xo_map[1] == self.xo_map[5] == self.xo_map[9] and isinstance(self.xo_map[1], str):
            return self.xo_map[1]
        if self.xo_map[3] == self.xo_map[5] == self.xo_map[7] and isinstance(self.xo_map[3], str):
            return self.xo_map[3]

        # return True

        # if self.xo_map[1] == self.xo_map[2] == self.xo_map[3] and isinstance(self.xo_map[1], str):
        #     return self.xo_map[1]
        # if self.xo_map[4] == self.xo_map[5] == self.xo_map[6] and isinstance(self.xo_map[4], str):
        #     return self.xo_map[4]
        # if self.xo_map[7] == self.xo_map[8] == self.xo_map[9] and isinstance(self.xo_map[7], str):
        #     return self.xo_map[7]
        # if self.xo_map[1] == self.xo_map[4] == self.xo_map[7] and isinstance(self.xo_map[1], str):
        #     return self.xo_map[1]
        # if self.xo_map[2] == self.xo_map[5] == self.xo_map[8] and isinstance(self.xo_map[2], str):
        #     return self.xo_map[2]
        # if self.xo_map[3] == self.xo_map[6] == self.xo_map[9]  and isinstance(self.xo_map[3], str):
        #     return self.xo_map[3]
        # if self.xo_map[1] == self.xo_map[5] == self.xo_map[9] and isinstance(self.xo_map[1], str):
        #     return self.xo_map[1]
        # if self.xo_map[3] == self.xo_map[5] == self.xo_map[7] and isinstance(self.xo_map[3], str):
        #     return self.xo_map[3]

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        sssign: str
        if isinstance(player, _Player):
            sssign = player.sign
        elif isinstance(player, str):
            sssign = player
        elif isinstance(player, int):
            if player == 1:
                sssign = self.player1.sign
            elif player == 2:
                sssign = self.player2.sign

        if isinstance(cell_no, int) and not 1 <= cell_no <= 9:
            raise Exception(cell_no, 'Enter a valid cell no [1, 9]')
        if self.xo_map[cell_no]:
            raise Exception(cell_no, "Cell is filled")

        sssign = str(sssign).lower()
        if sssign not in 'xo':
            raise Exception(sssign, 'Invalid sign')
        self.xo_map[cell_no] = sssign

    def winner(self) -> Optional[_Player]:
        result = self._calculate_result()
        # print(result)
        if result:

            if self.player1.sign == result:
                return self.player1.name
            elif self.player2.sign == result:
                return self.player2.name
        else:
            for i in range(1, 10):
                if not self.xo_map[i]:
                    return 'the game is not finished'

            return 'the game become equal'



a = _Player('yousef', 'x')

b = _Player('mohamad', 'o')

t1 = _XOGame(a, b)
print(t1)

while True:
    number = int(input('enter the place you want add a sign:'))
    s = input('enter ether (x and o) or player or player number:')
    for_exit = input("if you want to exit the game enter 'exit' or leave this : ")
    if s.isnumeric():
        int(s)
    # elif s == x or
    t1.mark(number, s)
    print(t1)
    if for_exit == 'exit':
        break


# t1.mark(3, 'x')
# print(t1)
#
# t1.mark(9, 2)
# print(t1)
#
# t1.mark(6, 1)
# print(t1)
#
# t1.mark(2, 2)
# print(t1)
#
# t1.mark(5, 1)
# print(t1)
#
# t1.mark(8, 1)
# print(t1)
#
# t1.mark(1, 1)
# print(t1)
#
# t1.mark(4, 2)
# print(t1)
#
# t1.mark(7, 2)
# print(t1)

#
# t1.mark(1,2)
# t1.mark(2,1)
# t1.mark(5,2)
# t1.mark(3,1)
# t1.mark(9,2)
# print(t1.xo_map)
w = t1.winner()
print(w)
