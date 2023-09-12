# Parse the function pointer in gMain.callback1 and gMain.callback2 to the function names from the game symbols
# Move this script to the root directory to ensure all imports work correctly
import struct
from modules.Console import console
from modules.Memory import GetGameState, ReadSymbol, mGBA


def AddrName(address: int):
    for key, (value, _) in mGBA.symbols.items():
        if value == address:
            return '{}: {}'.format(
                hex(address),
                key
            )
    return '{}: _unknown'.format(hex(address))

with console.status('', refresh_per_second=100) as status:
    previous1 = b''
    previous2 = b''
    while True:
        callback1 = ReadSymbol('gMain', 0, 4)  #gMain.callback1
        callback2 = ReadSymbol('gMain', 4, 4)  #gMain.callback2
        if callback1 != previous1:
            addr = int(struct.unpack('<I', callback1)[0]) - 1
            if addr != -1:
                console.print('callback1: {} State: {} '.format(AddrName(addr),GetGameState().name))
            previous1 = callback1
        if callback2 != previous2:
            addr = int(struct.unpack('<I', callback2)[0]) - 1
            if addr != -1:
                console.print('callback2: {} State: {} '.format(AddrName(addr),GetGameState().name))
            previous2 = callback2