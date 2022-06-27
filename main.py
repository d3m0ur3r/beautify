"""Beautifies code
Needs more work. Argparse."""
import re
from b_argparser import arg_parser
from debugger import debugger

# [const]
MAX_LINE_LENGTH = 120
LINE_DESIGN = '═'
# [end]


def read_file(file):
    """Test"""
    # ╔═════════════════╗
    # ║  [ READ FILE ]  ║
    # ╚═════════════════╝
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):

        if line:
            try:

                space_count = re.search(r'^(\s+)?#(\s\[\w+])$', line).group().count(' ')

                line = re.search(r'\w+', line).group()

                text = f'[ {line} ]'.upper() if line != 'end' else LINE_DESIGN
                text_len = len(text)
                # space_count = 0
                space_count -= 1

                front = LINE_DESIGN * ((((MAX_LINE_LENGTH - 4) - space_count) - text_len) // 2)
                back = LINE_DESIGN * ((((MAX_LINE_LENGTH - 4) - space_count) - text_len) // 2)

                if text_len % 2 != 0:
                    back += LINE_DESIGN

                lines[idx] = '{0}# {1}{2}{3} #\n'.format(space_count * ' ',
                                                         front,
                                                         text, back)

                print(f"{idx=} {line=}")
                print(lines[idx])
            except AttributeError as e:
                pass

    return lines


def main() -> int:
    args = arg_parser()

    file_path = args.file
    echo = args.echo
    changes = args.show_change
    if args.debug:
        debugger([f'Filepath:    {file_path}',
                  f'Echo:        {echo}',
                  f'Show_change: {changes}'])
        raise SystemExit(0)

    file = read_file(file_path)
    master_string = ""
    for x in file:
        master_string += x
    if echo:
        print(master_string)

    # with open(file_path, 'w', encoding='utf-8') as f:
    #     f.writelines(master_string)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
