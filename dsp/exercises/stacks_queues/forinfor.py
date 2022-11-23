# 9
# add     --> 1
# for 43
# end
# for 10     -------
#                  |
#   for 15         |
#     add          |
#   end            |  --->  10 * 16 == 160
#                  |
#   add            |
# end        -------
# --> 1 + 160 = 161
from typing import List


class For:
    def __init__(self, how_much: int):
        self.how_much: int = how_much
        self.how_much_add: int = 0

    def iterate_factor(self) -> int:
        return self.how_much * self.how_much_add

    def iterate(self, x: int) -> int:
        return x + self.iterate_factor()

    def __repr__(self):
        return f"{self.__class__.__name__}(how_much={self.how_much}, how_much_add={self.how_much_add})"


def _inter(args: list) -> int:
    return int(args[-1])


overflow = 2**32 - 1


def check_overflow(x: int) -> bool:
    return x > overflow


if __name__ == "__main__":
    stack: List["For"] = []

    count = int(input())
    global_x = 0

    for _ in range(count):
        command, *arg = input().split()
        if not stack and command == "add":
            global_x += 1
            if check_overflow(global_x):
                print("OVERFLOW")
                break
        elif stack:
            if command == "add":
                stack[-1].how_much_add += 1
            elif command == "end":
                last = stack.pop()
                if not stack:
                    global_x = last.iterate(global_x)
                    if check_overflow(global_x):
                        print("OVERFLOW")
                        break
                    continue
                stack[-1].how_much_add += last.iterate_factor()
            else:
                stack.append(For(_inter(arg)))
        else:
            stack.append(For(_inter(arg)))
    else:
        print(global_x)
