payloadhandlerem = {}
payloadhandleadd = {}
def namef(string):
    return int(string[3:], 10)

def payhandrem():
    payloadhandlerem[namef(func.__name__)] = func
    if __name__ == "__main__":
        print(f"reach : {namef(func.__name__)}")
    return func

def payhandadd():
    payloadhandleadd[namef(func.__name__)] = func
    if __name__ == "__main__":
        print(f"reach : {namef(func.__name__)}")
    return func

@payhandadd
def add688488103253508099(b, payload):
    try:
        role, member, emoji_name = self.get_role_member(payload)
        await member.add_roles(role)
        await member.send(f":white_check_mark: Tu as maintenant accès aux salons {emoji_name} , Bon travail !")
    except:
        await member.send("Erreur lors de l'attribution du rôle , contacte un administrateur ( Raphaël PEYRE en priorité )")

@payhandrem
def rem688493645351092285(b, payload):
    try:
        role, member, emoji_name = self.get_role_member(payload)
        await member.remove_roles(role)
        await member.send(f":x: Tu ne peux maintenant plus accèder aux salons {emoji_name} !")
    except:
        pass
