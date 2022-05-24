def debugger(debugger_list: list):
    """Debugger menu"""

    # debugger_list = [f"Remote Path:    {self.remote_path}",
    #                  f"Local Path:     {self.local_path}",
    #                  f"Username:       {self.username}",
    #                  f"Password:       {self.password}",
    #                  f"Reverse:        {self.reverse}",
    #                  f"Mirror:         {self.mirror}",
    #                  f"Extension:      {self.extension}",
    #                  f"Port:           {self.port}",
    #                  f"Transfer Files: {self.transfer_files}"]

    max_length = max([len(x) for x in debugger_list])
    padding = 3
    spacer = " " * padding
    padding_calculation = max_length + (padding * 2)
    debugger_list = [f"║{spacer}{x.ljust(max_length)}{spacer}║" for x in debugger_list]

    debug_top = f"╔{'═' * padding_calculation}╗"
    debug_top_msg = f"║{'DEBUGGER'.center(padding_calculation)}║"
    debug_top_bar = f"{'╠' + ('═' * padding_calculation) + '╣'}"
    debug_bottom = f"╚{'═' * padding_calculation}╝"

    for index, d in enumerate(debugger_list):
        d = list(d)
        for i, x in enumerate(d):
            if x not in ['║']:
                d[i] = f"\x1b[1m{x}\x1b[0m"
        debugger_list[index] = "".join(d)

    debugger_list.insert(0, debug_top)
    debugger_list.insert(1, debug_top_msg)
    debugger_list.insert(2, debug_top_bar)
    debugger_list.append(debug_bottom)

    _ = *map(print, debugger_list),


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
