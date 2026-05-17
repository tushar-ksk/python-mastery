import time
import random

# --- Data Structures ---
CHARACTERS = {
    "hero": {"name": "Hero", "level": 1, "xp": 0, "xp_to_next_level": 100, "health": 100, "max_health": 100, "attack": 10, "defense": 5, "inventory": {"gold": 50, "potion": 1}, "equipped_weapon": "Rusty Sword"},
    "goblin": {"name": "Goblin", "health": 30, "attack": 8, "defense": 2, "gold": 15, "xp": 40},
    "orc": {"name": "Orc", "health": 60, "attack": 15, "defense": 5, "gold": 40, "xp": 100},
}

WEAPONS = {
    "Rusty Sword": {"attack": 5, "cost": 0},
    "Iron Sword": {"attack": 12, "cost": 50},
    "Steel Sword": {"attack": 20, "cost": 150},
}

ITEMS = {"potion": {"heal": 40, "cost": 20}}

DESTINATIONS = {
    "village": {
        "desc": "A safe haven with a merchant and a guard.",
        "paths": ["forest", "mountains"],
        "npcs": ["merchant", "guard"],
        "shop": ["potion", "Iron Sword", "Steel Sword"]
    },
    "forest": {
        "desc": "Dark trees surround you. Goblins lurk here.",
        "paths": ["village", "clearing"],
        "enemies": ["goblin"]
    },
    "clearing": {
        "desc": "A quiet spot deep in the woods.",
        "paths": ["forest"],
        "enemies": ["goblin"]
    },
    "mountains": {
        "desc": "High peaks where dangerous Orcs roam.",
        "paths": ["village"],
        "enemies": ["orc"]
    }
}

# --- Game State ---
player = CHARACTERS["hero"]
location = "village"
game_log = ["Game started! You are in the village."]
enemy = None

# --- Logic Functions ---
def add_log(msg):
    game_log.append(msg)
    if len(game_log) > 6: game_log.pop(0)

def level_up():
    if player["xp"] >= player["xp_to_next_level"]:
        player["level"] += 1
        player["xp"] -= player["xp_to_next_level"]
        player["xp_to_next_level"] = int(player["xp_to_next_level"] * 1.5)
        player["max_health"] += 20
        player["health"] = player["max_health"]
        player["attack"] += 3
        add_log(f"LEVEL UP! You are now level {player['level']}!")

def combat_tick(action):
    global enemy
    if not enemy: return

    # Player hit
    p_atk = player["attack"] + WEAPONS[player["equipped_weapon"]]["attack"]
    dmg = max(1, p_atk - enemy["defense"])
    enemy["health"] -= dmg
    add_log(f"You hit {enemy['name']} for {dmg}!")

    if enemy["health"] <= 0:
        add_log(f"Victory! Gained {enemy['xp']} XP and {enemy['gold']} gold.")
        player["xp"] += enemy["xp"]
        player["inventory"]["gold"] += enemy["gold"]
        enemy = None
        level_up()
        return

    # Enemy hit
    e_dmg = max(1, enemy["attack"] - player["defense"])
    player["health"] -= e_dmg
    add_log(f"{enemy['name']} hits you for {e_dmg}!")

def draw_ui():
    print("\n" * 20) # Clear screen
    print("=" * 40)
    print(f" PLAYER: {player['health']}/{player['max_health']} HP | Gold: {player['inventory']['gold']}")
    print(f" WEAPON: {player['equipped_weapon']} | Level: {player['level']}")
    print("=" * 40)
    
    if enemy:
        print(f" !!! BATTLE: {enemy['name']} (HP: {enemy['health']}) !!!")
    else:
        print(f" LOCATION: {location.upper()}")
        print(f" {DESTINATIONS[location]['desc']}")
        print(f" PATHS: {', '.join(DESTINATIONS[location]['paths'])}")
    
    print("-" * 40)
    for msg in game_log: print(f"> {msg}")
    print("-" * 40)

# --- Main Loop ---
while player["health"] > 0:
    draw_ui()
    cmd = input("Command: ").lower().split()
    if not cmd: continue
    
    action = cmd[0]
    target = cmd[1] if len(cmd) > 1 else None

    # Combat Mode
    if enemy:
        if action == "attack": combat_tick("attack")
        elif action == "use" and target == "potion":
            if player["inventory"].get("potion", 0) > 0:
                player["health"] = min(player["max_health"], player["health"] + 40)
                player["inventory"]["potion"] -= 1
                add_log("Used Potion.")
                combat_tick("wait") # Enemy still hits you
            else: add_log("No potions!")
        else: add_log("You are in combat! Attack or use potion.")
        continue

    # Exploration Mode
    if action == "go" and target in DESTINATIONS[location]["paths"]:
        location = target
        add_log(f"Moved to {target}.")
        # Random Encounter
        if "enemies" in DESTINATIONS[location] and random.random() < 0.6:
            ename = random.choice(DESTINATIONS[location]["enemies"])
            enemy = CHARACTERS[ename].copy()
            add_log(f"A wild {ename} appeared!")
            
    elif action == "shop":
        if "shop" in DESTINATIONS[location]:
            print("\n--- SHOP ---")
            for item in DESTINATIONS[location]["shop"]:
                cost = ITEMS[item]["cost"] if item in ITEMS else WEAPONS[item]["cost"]
                print(f"- {item}: {cost} gold")
            buy = input("Type item name to buy (or 'cancel'): ")
            if buy in DESTINATIONS[location]["shop"]:
                cost = ITEMS[buy]["cost"] if buy in ITEMS else WEAPONS[buy]["cost"]
                if player["inventory"]["gold"] >= cost:
                    player["inventory"]["gold"] -= cost
                    if buy in WEAPONS:
                        player["equipped_weapon"] = buy
                        add_log(f"Equipped {buy}!")
                    else:
                        player["inventory"][buy] = player["inventory"].get(buy, 0) + 1
                        add_log(f"Bought {buy}.")
                else: add_log("Not enough gold!")
        else: add_log("No shop here.")

    elif action == "use" and target == "potion":
        if player["inventory"].get("potion", 0) > 0:
            player["health"] = min(player["max_health"], player["health"] + 40)
            player["inventory"]["potion"] -= 1
            add_log("Healed up!")
        else: add_log("No potions!")

    elif action == "help":
        add_log("Commands: go [loc], shop, use potion, attack")

print("\n--- GAME OVER ---")
print("You succumbed to your injuries. Better luck next time!")