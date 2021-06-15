from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzgBu5LPN9GXbHFu8LUpfxfs-IXPB-VBLPBSiANFUW5mimcWDdvT2uWDxZZETG7PxmQImsnqBHEYsdELekmL-34Q8LrMqqEDS_Jt32xpr4QNktC6_BOMoRLdAt3asia0CmaCkojpFpelnPZoEBSs9gt9VatD0Z69dSDN9CTpb1POgY8cAcscM2WRkuRtM9hLg5NDfaj6BqpYGLLmOwPUPiDUJwcB90W-OiDfjJ6wyxW4Tp861mmDx2qZktRP7lLuIfvpJDwyjTTaKFiQHfEy4LhBRl1BXtwj2IkddYOLXXm2XRzptM7vzHr2YzX1-yw1qXDSkpMJVvXwJSNSdsKTIF-r7Cc=")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAG_qNWSYnl1jEUvAnhaqLrXUFONUKObIJM")
BOT_NAME = getenv("BOT_NAME", "musicbot")
admins = {}
API_ID = int(getenv("API_ID", "3088812"))
API_HASH = getenv("API_HASH", "d51f13802ef40ccb115e333a5f9dc9e7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1801516703").split()))
