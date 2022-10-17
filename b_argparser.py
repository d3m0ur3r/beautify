import sys
import argparse

banner = """\x1b[1;31m
$$$$$$$\                                  $$\     $$\  $$$$$$\            
$$  __$$\                                 $$ |    \__|$$  __$$\           
$$ |  $$ | $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\   $$\ $$ /  \__|$$\   $$\ 
$$$$$$$\ |$$  __$$\  \____$$\ $$ |  $$ |\_$$  _|  $$ |$$$$\     $$ |  $$ |
$$  __$$\ $$$$$$$$ | $$$$$$$ |$$ |  $$ |  $$ |    $$ |$$  _|    $$ |  $$ |
$$ |  $$ |$$   ____|$$  __$$ |$$ |  $$ |  $$ |$$\ $$ |$$ |      $$ |  $$ |
$$$$$$$  |\$$$$$$$\ \$$$$$$$ |\$$$$$$  |  \$$$$  |$$ |$$ |      \$$$$$$$ |
\_______/  \_______| \_______| \______/    \____/ \__|\__|       \____$$ |
                                                                $$\   $$ |
                                                                \$$$$$$  |
                                                                 \______/ 
\x1b[0m"""


def arg_parser() -> argparse.Namespace:
    # ArgParser - Define Usage
    prog_name = sys.argv[0]
    parser = argparse.ArgumentParser(prog=prog_name,
                                     epilog=r"""
Usage:
Edit your script like so:

 # [Your text reference]
<Your code here>
 # [end]

╔══════════════════════════════════════[ Examples ]═════════════════════════════════════╗                                         
║  -f ~/my_file.py                                                                      ║
║  -e -f C:\Users\MyUser\my_file.py                                                     ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
""",
                                     usage=f"{prog_name}",
                                     prefix_chars="-",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-f', '--file',
                        action='store',
                        metavar='File',
                        type=str,
                        required=True,
                        help=r'Filepath to be beautified')

    parser.add_argument('-e', '--echo',
                        action='store_true',
                        default=True,
                        help='Echo to screen without doing any changes.')

    parser.add_argument('-d', '--do-change',
                        action='store_true',
                        help='Does change.')

    parser.add_argument('--debug',
                        action='store_true',
                        help=argparse.SUPPRESS)

    parser.add_argument('-v', action='version',
                        version=f'{banner}'
                                f'\nBeautify'
                                f'\nv0.1 by \x1b[1;3;31md3m0ur3r\x1b[0m ',
                        help=f'Prints the version of {prog_name}')

    args = parser.parse_args()  # Engages ArgParser

    # ═══════════════════════════════════════════════[ ARGS ]════════════════════════════════════════════════════ #

    # ═══════════════════════════════════════════════════════════════════════════════════════════════════════════ #

    return args


def main() -> int:
    print(arg_parser())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
