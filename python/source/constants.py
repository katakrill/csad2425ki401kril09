SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

CELLS_NUMBER = 3
FPS = 120

DARK_COLOR = (135, 108, 50)
LIGHT_COLOR = (224, 189, 112)
FIGURE_COLOR = (255, 236, 194)

FIGURE_WIDTH = 10
EMPTY_POSITION = ((-1, -1), "")

RECEIVE_BUFFER_LENGTH = 11
SEND_BUFFER_LENGTH = 2

PACKET_START_VALUE = b'<'
PACKET_END_VALUE = b'>'

WIN_MASKS = [
    [0xFF, 0xFF, 0xFF, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0xFF, 0xFF, 0xFF, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0xFF, 0xFF, 0xFF],
    [0xFF, 0, 0, 0xFF, 0, 0, 0xFF, 0, 0],
    [0, 0xFF, 0, 0, 0xFF, 0, 0, 0xFF, 0],
    [0, 0, 0xFF, 0, 0, 0xFF, 0, 0, 0xFF],
    [0xFF, 0, 0, 0, 0xFF, 0, 0, 0, 0xFF],
    [0, 0, 0xFF, 0, 0xFF, 0, 0xFF, 0, 0],
]

MAN_VS_MAN_PACKET = bytes([0xBB for _ in range(SEND_BUFFER_LENGTH)])
MAN_VS_AI_PACKET = bytes([0xCC for _ in range(SEND_BUFFER_LENGTH)])
AI_VS_AI_PACKET = bytes([0xDD for _ in range(SEND_BUFFER_LENGTH)])
RESET_PACKET = bytes([0x99 for _ in range(SEND_BUFFER_LENGTH)])
DUMMY_PACKET = bytes([0x33 for _ in range(SEND_BUFFER_LENGTH)])
WIN_NOD_PACKET = bytes([0x77 for _ in range(SEND_BUFFER_LENGTH)])
WIN_CROSS_PACKET = bytes([0x88 for _ in range(SEND_BUFFER_LENGTH)])
NO_WINNER_PACKET = bytes([0x22 for _ in range(SEND_BUFFER_LENGTH)])

ACK_PACKET = bytes([0xEE for _ in range(CELLS_NUMBER ** 2)])

GAME_TYPE_MENU = 0
GAME_TYPE_MVM = 1
GAME_TYPE_MVA = 2
GAME_TYPE_AVA = 3

CAPTION = "Ісак Володимир Варіант №9"

PSOC_WRITE_CHARACTERISTIC = "87388F31-37CD-485A-A724-387EADD6AFDB"
PSOC_READ_CHARACTERISTIC = "14B52F65-E172-4E76-B8FB-809532F92CA0"
PSOC_ADDRESS = "00:A0:50:E8:C8:9B"
PSOC_COM = "COM40"
