from WakeUp import Wake
from FantaConverter import Convertify
from OSPoint import Executer

class StringType(Convertify.String):
    ...

class Fansole(object):
    def loadingAnimate(msg: str | StringType, sleeper: int | Wake = 0.08, forGround: int | Wake = 1):
        party = [
            " < ",
            " ^ ",
            " > ",
            " < ",
            " ^ ",
            " > ",
            " / ",
            " | ",
            " _ ",
            " \\ "
        ]

        for _ in range(forGround):
            for item in party:
                print(f"\r{msg} {item}", flush=True, end="")
                Wake.onSleep(sleeper)

    def rePlaceAnimatedMsg(msg: str | StringType, animatedMsg: str | StringType):
        print(f"\r{msg}", flush=True, end=" "*(len(animatedMsg)-len(msg)+3))

    def colorizes():
        Executer.command("")

        for i in range(258):
            print(f'\001\033[0;38;5;{i}m\002Hello World: color code {i}')
        
        print("""\001\033[0;38;5;{i}m\002""")

    class PadEnd(object):
        def __init__(self) -> None:
            pass
        
        def simple(self, a: str, b: str, __much: int):
            print("{:<{}} {:<}".format(a, __much, b))

        def liner(self, a: str, b: str, __much: int):
            print("{:<{}} {:<}".format(a, __much, b))
            x = __much +  len(b) + 2
            print("-"*x)

        def postive(self, a: str, b:str, __much: int):
            print("{:<{}} {:<}".format(a, __much, b))
            x = __much + len(b) + 2
            print("+"*x)

        def mul(self, a: str, b: str, __much: int):
            print("{:<{}} {:<}".format(a, __much, b))
            x = __much + len(b) + 2
            print("*"*x)

        def eql(self, a: str, b: str, __much: int):
            print("{:<{}} {}".format(a, __much, b))
            x = __much + len(b) + 2
            print("="*x)

        def hashtag(self, a: str, b: str, __much: int):
            print("{:<{}} {}".format(a, __much, b))
            x = __much + len(b) + 2
            print("#"*x)

        def formatter(self, a: str, b: str, __much: int):
            print("{:<{}} {}".format(a, __much, b))
            x1 = __much + len(b) + 2

            if x1 % 2 == 0:
                print("{}{}".format("{"*int(x1 / 2),"}"*int(x1 / 2)))

            else:
                print("{}{}".format("{"*int(x1 / 2 + 1),"}"*int(x1 / 2 + 1)))

        def formatterData(self, a: str, b: str, data: str, __much: int):
            print("{:<{}} {}".format(a, __much, " "*(len(b) - 3)+b))
            x1 = __much + len(b) + 2

            if x1 % 2 == 0:
                print("{}{}{}".format("{"*int(x1 / 2), data, "}"*int(x1 / 2 - len(data) + 2)))

            else:
                print("{}{}{}".format("{"*int(x1 / 2 + 1), data, "}"*int(x1 / 2 - len(data) + 3)))