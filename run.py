import os, config, ansicolors as ac
from ansicolors import clp, fg, bg
os.system('cls || clear')

clp(f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{fg.magenta}⣫{fg.green}⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇{fg.magenta}⣿⣿⣮{fg.green}⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿{fg.magenta}⣾⣿⣿⣿⣷{fg.green}⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟{fg.magenta}⣽⣿⣿⣿⣿⣿⣿{fg.green}⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿{fg.magenta}⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮{fg.green}⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿{fg.magenta}⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷{fg.green}⡿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿{fg.magenta}⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷{fg.green}⡽⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿{fg.magenta}⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{fg.green}⡽⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿{fg.magenta}⢧⣿⣿⣿⣿⠿⠿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠛{fg.green}⠻⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⡅{fg.white}⠀⠀⠀⠀⣀⣀⣀⣀⣀⡈⠢⡀⠀⠀⠀⣀⣀⣀⣀⣈{fg.green}⡻⣿
⣿⣿⣿⣿⡿⠁{fg.white}⠈⠀⠀⠀⠘⠻⣿⡿⠛⡍⠉⠙⣿⡆⣒⣈⣥⣤⣶⢖⠒{fg.green}⢲⣶⣽
⣿⣿⣿⣿⠃{fg.white}⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠂⠀⠁⣨⠜⠿⠿⣿⣿⠁⠀⠰⠀⢋{fg.green}⣾
⣿⣿⣿⡿{fg.white}⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠩⠝⠊⠀⢀⣀⣀⣀⣐⣒⣒⣁{fg.green}⣿⣿
⣿⣿⣿⡇{fg.white}⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣛⣓⠲⠖⠒⠋⢉⣉⠩⠥⢐{fg.green}⣶⣽⣷⣿⣿
⣿⣿⣿⣷⡀{fg.white}⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀{fg.green}⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷                {fg.blue}⣴⣶⣝{fg.green}⢿⣿⣿⣿⣿⣿
⣿⡿{fg.blue}⣵⣿⣿⣿⣿⣶⣯⣭⣭⣽⣿⣿⣯⣭⣭⣽⣶⣿⣿⣿⣿⣿⣷{fg.green}⢻⣿⣿⣿⣿
⡟{fg.blue}⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{fg.green}⣿⣿⣿⣿
""",fg.green)


 
clp("RSIemaCross, EmaCross", fg.black, bg.white)
arewetesting = input("Are you currently testing? y/n: ").lower()
if arewetesting == 'y':
    config.testing = True
elif arewetesting == 'n':
    config.testing = False
strat = input("What strategy would you like to run? ")
os.system(f'python {strat}.py')