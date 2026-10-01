import json


def new_game():
    return {'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_21(state):
    target = state["src"]
    for start, end in state["events"].values():
        if start <= target < end:
            return False
    return True

def bug_28(state):
    weight = state["dst"] - state["src"]
    return weight >= 0

def bug_5(state):
    return state["queue"][0] if state["queue"] else None

def bug_12(state):
    amount = 10
    if amount < 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_19(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def bug_26(state):
    start, end = state["src"], state["dst"]
    if start < 0 or end < 0 or start >= end:
        return False
    return True

def bug_3(state):
    return state["queue"].pop(0) if state["queue"] else None

def bug_10(state):
    amount = -5
    if amount < 0:
        return False
    state["amount"] += amount
    return True

def bug_17(state):
    amount = -5
    if amount < 0 or state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_24(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_30(state):
    if any(entry[-1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        state["log"] = []
        return False
    return True

def bug_31(state):
    return not state["settled"]

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
