
import os
os.system('color')
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m' # called to return to standard terminal text color
def write_black(x):
   print(BLACK + x + RESET)
def write_red(x):
   print(RED + x + RESET)
def write_green(x):
   print(GREEN + x + RESET)
def write_yellow(x):
   print(YELLOW + x + RESET)
def write_blue(x):
   print(BLUE + x + RESET)
def write_cyan(x):
   print(CYAN + x + RESET)
def write_bred(x):
   print(BRIGHT_RED + x + RESET)
def write_bgreen(x):
   print(BRIGHT_GREEN + x + RESET)
def write_byellow(x):
   print(BRIGHT_YELLOW + x + RESET)
def write_bblue(x):
   print(BRIGHT_BLUE + x + RESET)
def write_bcyan(x):
   print(BRIGHT_CYAN + x + RESET)
def write_white(x):
   print(WHITE + x + RESET)