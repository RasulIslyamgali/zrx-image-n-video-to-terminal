from subprocess import call

REDUCE_FONT_SIZE_COMMAND = 'ctrl+minus'


def minimize_terminal_font_size(cycle_count: int = 20):
    for i in range(cycle_count):
        call(["xdotool", "key", REDUCE_FONT_SIZE_COMMAND])
