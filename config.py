from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCRst05jrHhXEJEi2e_BxsHcCu_Gx-0xILsYtPasXDc4bjWqH7cHYJQKN6f8V07hfo5AV81Ikj4k0xPPK8WuxddEBmxmRsUljWTq8E7Dm1BRHnnXicvjpqGhdfAbMfqKt9pXprURqwqTiNQWDkBMAK-qjUucVY6XZ3HNi7K61DcRosBo3lZWyhfA2afA2BCgFYxQA8zDQdpSUG4Jlzrmt-2ido7b4HGOgzLql0SH-z-EChqngjCCTztBIOXC9vRY_HbmFXK9WhwXiHf64HnlW-B-fya9bkZHJwpM-p5ZbBqWydikVuz6oV3Fb6tns0CCfSnVEs2X8ZjZZGnhWPm7bFXL7y8qgA")
BOT_TOKEN = getenv("BOT_TOKEN", "1883531251:AAENwbKG7JRGGZGz65i5_2yVT3AXgPOkZUU")
BOT_NAME = getenv("BOT_NAME", "musicbot")
admins = {}
API_ID = int(getenv("API_ID", "3088812"))
API_HASH = getenv("API_HASH", "d51f13802ef40ccb115e333a5f9dc9e7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1801516703").split()))
