"""Beautifies code
Needs more work. Argparse."""
import re
from b_argparser import arg_parser
from debugger import debugger


def read_file(file):
    """Test"""
    # ╔═════════════════╗
    # ║  [ READ FILE ]  ║
    # ╚═════════════════╝
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    max_line_length = 120
    line_design = '═'
    blank_design = '═'
    for idx, line in enumerate(lines):

        if line:
            try:

                space_count = re.search(r'^(\s+)?#(\s\[\w+])$', line).group().count(' ')

                line = re.search(r'\w+', line).group()

                text = f'[ {line} ]'.upper() if line != 'end' else line_design
                text_len = len(text)
                # space_count = 0
                space_count -= 1

                front = line_design * ((((max_line_length - 4) - space_count) - text_len) // 2)
                back = line_design * ((((max_line_length - 4) - space_count) - text_len) // 2)

                if text_len % 2 != 0:
                    back += line_design

                # blanks = '{0}# {1} #{2}'.format(space_count * ' ', blank_design * ((max_line_length - space_count) - 4),
                #                                 '\n' if line != 'end' else '')
                # blanks = blanks + '\n' if line == 'end' else blanks
                # lines[idx] = '{0}{1}# {2}{3}{4} #\n{5}'.format(blanks if line != 'end' else '', space_count * ' ',
                #                                                front,
                #                                                text, back, blanks if line == 'end' else '')
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
    if args.debug:
        debugger([f'Filepath: {file_path}'])
        raise SystemExit(0)
    file = read_file(file_path)
    master_string = ""
    for x in file:
        master_string += x
    # print(master_string)

    # with open(file_path, 'w', encoding='utf-8') as f:
    #     f.writelines(master_string)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
