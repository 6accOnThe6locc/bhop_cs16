from time import sleep

from keyboard import is_pressed
from pymem import Pymem, process


FORCE_JUMP_ADDRESS = 0x12D048
ON_GROUND_ADDRESS = 0x11FDAB4


class BunnyHop:
    def __init__(self) -> None:
        self.game_handle = Pymem('hl.exe')
        self.client_dll = process.module_from_name(
            self.game_handle.process_handle, 'client.dll'
        ).lpBaseOfDll
        self.hw_dll = process.module_from_name(
            self.game_handle.process_handle, 'hw.dll'
        ).lpBaseOfDll
        self.delay_jump = 0.05
        self.active_key = 'space'

    def on_ground(self) -> None:
        return self.game_handle.read_int(self.hw_dll + ON_GROUND_ADDRESS) == 1

    def jump(self) -> None:
        if self.on_ground():
            self.game_handle.write_int(self.client_dll + FORCE_JUMP_ADDRESS, 5)
            sleep(self.delay_jump)
            self.game_handle.write_int(self.client_dll + FORCE_JUMP_ADDRESS, 4)

    def run(self) -> None:
        while True:
            if is_pressed(self.active_key):
                self.jump()


def main():
    bunny = BunnyHop()
    bunny.run()


if __name__ == '__main__':
    main()
