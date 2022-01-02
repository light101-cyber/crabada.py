from src.common.config import users
from src.libs.CrabadaWeb2Client.CrabadaWeb2Client import CrabadaWeb2Client
from pprint import pprint

# VARS
client = CrabadaWeb2Client()
userAddress = users[0]['address']

# TEST FUNCTIONS
def testGetOpenMines() -> None:
    params = {"limit": 5, "page": 1, "status": "open"}
    pprint(client.listMines(userAddress, params=params).json())

def testGetAllMines() -> None:
    pprint(client.listMines(userAddress).json())

# EXECUTE
print(">>> OPEN MINES/GAMES")
testGetOpenMines()
print(">>> ALL MINES/GAMES")
testGetAllMines()