import sqlite3
import requests
import json
import re
from enum import Enum

DB_CONNECTION = sqlite3.connect("suvbot.db") # takzvane mrdam vam mongo, proste to udelam jednoduse
DB_CURSOR = DB_CONNECTION.cursor()

class AddTrackedRewardReturns(Enum):
    OK = 0
    ALREADY_PRESENT = 1
    INVALID = -1

with open("warframe/invasion_rewards.txt", "r") as invasion_rewards_file:
    INVASION_REWARD_LIST = invasion_rewards_file.read().split("\n")

def split_words_with_capital(text) -> str:
    # Use regular expression to split words starting with a capital letter
    words = re.findall('[A-Z][a-z]*', text)
    ret = ""

    for x in words:
        if x == words[0]:
            ret += x
        else:
            ret += f" {x}"
    
    return ret

async def get_tracked_invasions() -> list[tuple]:
    res = DB_CURSOR.execute("SELECT * FROM active_invasions")
    return res.fetchall()

async def add_tracked_invasion(reward1:str, reward2:str) -> None:
    DB_CURSOR.execute(f"INSERT INTO active_invasions (reward1, reward2) VALUES ('{reward1}', '{reward2}')")
    DB_CONNECTION.commit()
    return

async def remove_tracked_invasion(reward1:str, reward2:str) -> None:
    DB_CURSOR.execute(f"DELETE FROM active_invasions WHERE reward1='{reward1}' AND reward2='{reward2}'")
    DB_CONNECTION.commit()

async def get_tracked_rewards() -> list[str]:
    res = DB_CURSOR.execute("SELECT * FROM tracked_rewards")
    ret = []
    for x in res.fetchall():
        ret.append(x[0])
    return ret

#returns are based on the AddTrackedRewardReturns enum class god knows how this works in python
async def add_tracked_reward(reward:str) -> AddTrackedRewardReturns:
    if not reward in INVASION_REWARD_LIST:
        return AddTrackedRewardReturns.INVALID
    
    tracked_rewards = await get_tracked_rewards()

    if reward in tracked_rewards:
        return AddTrackedRewardReturns.ALREADY_PRESENT
    
    DB_CURSOR.execute(f"INSERT INTO tracked_rewards (reward) VALUES ('{reward}')")
    DB_CONNECTION.commit()
    return AddTrackedRewardReturns.OK
    
async def remove_tracked_reward(reward:str) -> None:
    DB_CURSOR.execute(f"DELETE FROM tracked_rewards WHERE reward='{reward}'")
    DB_CONNECTION.commit()

async def get_worldstate() -> dict:
    res = requests.get("https://content.warframe.com/dynamic/worldState.php")
    return res.json()

async def get_active_invasions() -> list[tuple]:
    ws = await get_worldstate()

    invasions = []

    for x in ws["Invasions"]:
        if x["Completed"]: continue
        reward1_raw:str = x["DefenderReward"]["countedItems"][0]["ItemType"]
        reward1 = split_words_with_capital(reward1_raw.split("/")[-1])

        try:
            reward2_raw:str = x["AttackerReward"]["countedItems"][0]["ItemType"]
            reward2 = split_words_with_capital(reward2_raw.split("/")[-1])
        except:
            reward2 = ""

        invasions.append((reward1,reward2))

    return invasions

async def update_tracked_invasions(send_message) -> None:
    active = await get_active_invasions()
    tracked = await get_tracked_invasions()
    tracked_rewards = await get_tracked_rewards()

    # first clean up those that are not active anymore
    for x in tracked:
        if not x in active:
            await remove_tracked_invasion(x[0], x[1])
    
    # then add those that we want to track
    for x in active:
        if x in tracked: continue
        if x[0] in tracked_rewards or x[1] in tracked_rewards:
            await add_tracked_invasion(x[0], x[1])
            await send_message(x[0], x[1])