import json
import sqlite3
import asyncio

import requests

db_connection = sqlite3.connect("suvbot.db")
db_cursor = db_connection.cursor()

try: db_cursor.execute("CREATE TABLE active_invasions(reward1, reward2)")
except: pass
try: db_cursor.execute("CREATE TABLE tracked_rewards(reward)")
except: pass
try: db_cursor.execute("CREATE TABLE saved_quotes(guild_id, channel_id, message_id UNIQUE, message_content, locked)")
except: pass

#db_cursor.execute("INSERT INTO active_invasions (reward1, reward2, planet, mission_type) VALUES ('testval1', 'testval2', 'hirukovamama', 'speedrun');")
#db_connection.commit()

#res = db_cursor.execute("SELECT * FROM tracked_rewards")
#print(type(res.fetchall()[0]))

#from warframe import get_worldstate, get_active_invasions

#loop = asyncio.get_event_loop()
#res = loop.run_until_complete(get_active_invasions())
#loop.close()

#print(res)