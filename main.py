"""Beautifies code
Needs more work. Argparse."""
import re
from b_argparser import arg_parser
from debugger import debugger

# [const]
MAX_LINE_LENGTH = 120
LINE_DESIGN = '═'


# [end]


def read_file(file: str) -> list:
    """Test"""
    # ╔═════════════════╗
    # ║  [ READ FILE ]  ║
    # ╚═════════════════╝
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):

        if line:

            try:
                space_count_before: str = re.search(r'^\s+#', line).group()
                space_count_before: int = space_count_before.count(' ')
            except AttributeError:
                space_count_before: int = 0

            try:
                space_count_after = re.search(r'#\s(\[[\w\s]+])$', line).group()
                space_count_after = space_count_after.count(' ')
                print(line, space_count_after)
                line = re.findall(r'\w+', line)
                line = " ".join(line)
                text = f'[ {line} ]'.title() if line != 'end' else LINE_DESIGN
                text_len = len(text)
                # space_count_after = 0
                space_count_after -= 1

                if space_count_after % 2 != 0:
                    spacer = 1
                else:
                    spacer = 0

                front = LINE_DESIGN * (
                            (((MAX_LINE_LENGTH - 4) + space_count_after - space_count_before) - text_len) // 2)
                back = LINE_DESIGN * (
                            (((MAX_LINE_LENGTH - 4) - space_count_after - space_count_before) - spacer - text_len) // 2)

                if text_len % 2 != 0:
                    back += LINE_DESIGN

                lines[idx] = '{0}# {1}{2}{3} #\n'.format(space_count_before * ' ',
                                                         front,
                                                         text, back)

                # print(f"{idx=} {line=}")
                # print(lines[idx])
            except AttributeError:
                pass

    return lines


def main() -> int:
    args = arg_parser()

    file_path: str = args.file
    echo: bool = args.echo
    do_change: bool = args.do_change

    if args.debug:
        debugger([f'Filepath:    {file_path}',
                  f'Echo:        {echo}',
                  f'Show_change: {do_change}'])
        raise SystemExit(0)

    file: list = read_file(file_path)
    master_string: str = ''.join(file)
    highlighted_list = ''.join([f'\x1b[1;37;100m{i:0>2}:\x1b[0m {f}' for i, f in enumerate(file, 1)])

    if echo and do_change:
        print(highlighted_list)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(master_string)
    elif echo:
        print(highlighted_list)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
