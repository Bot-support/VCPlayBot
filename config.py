from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA81xAnnLeJRA0JYt20jfAky1gEtrf8hgeIeSL_r1y-pCOCypCcYZ56pG_8pMdg79WMA2SUtreZ22pJ_GtkKBcD3dHFE1pIhOJDOaZ17DDWDSW3oWE87v4OZ3iEPapxIY1nei6eeTwuuuPCCCxSQcqGYpG2JAisrSWInrsvoBSj-cPHyCC5Zd0MpHspxVojaQZE0b5qIm4wvyNANl-CeLMN2sVxOqfm69-EUkBMhSeeQyykEuY0knXI8-RJ1xCLYIZWzecp_pXMRJe2fX9SWkG0x4Cs42Toh4xI1QJtox3DTG43Gi9rhjx8k5vnPj-4krpnvjPcD69Ln6kgMePQ5dVtb6crEAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAG_qNWSYnl1jEUvAnhaqLrXUFONUKObIJM")
BOT_NAME = getenv("BOT_NAME", "musicbot")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1801516703").split()))
