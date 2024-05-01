from Console import Fansole

pad = Fansole.PadEnd()

version = "4.4.4"

pad.simple("\001\033[0;38;5;15m\002Fanta", f"\001\033[0;38;5;87m\002{version}", 15)
pad.simple("\001\033[0;38;5;15m\002Created By", "\033[4m\001\033[0;38;5;93m\002github.com/Zrexer\033[00m")
print()