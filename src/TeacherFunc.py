from Cours import *
from ErrorsEq import *

commdict = {}
helphandler = {}


def namef(name):
    to_split = False
    if name[-2:] == '_h':
        name = name[:-2]
    while name[0] == '_':
        if len(name) == 1:
            return ''
        name = name[1:]
    for i in range(len(name)):
        if name[i] == '_':
            to_split = True
    if to_split:
        array = name.split("_")
        name = "-".join(array)
    return name

def helpwrap(func):
    helphandler[namef(func.__name__)] = func
    if __name__ == "__main__":
        print(f"reach helper : {namef(func.__name__)}")
    return func

def commwrap(func):
    commdict[namef(func.__name__)] = func
    if __name__ == "__main__":
        print(f"reach : {namef(func.__name__)}")
    return func


@commwrap
async def __(b, message):
    await message.channel.send(f'Commande inconnue : {message.content}')

@helpwrap
async def ___h(b, message, token_s):
    await message.channel.send("Besoin d'aide à porpos de error")

@commwrap
async def _print(b, message, token_s):
    print(''.join([c[0] for c in token_s[1:]]))
    await message.channel.send(''.join([c[0] for c in token_s[1:]]))

@helpwrap
async def _print_h(b, message, token_s):
    await message.channel.send("Besoin d'aide à porpos de la commande print ?")

@commwrap
async def arbitrary_exec(b, message, token_s):
    rv = None
    try:
        rv = eval(' '.join([c[0] for c in token_s[1:]]), globals(), locals())
    except Exception as e:
        message.channel.send(str(e))
    message.channel.send(str(rv))

@commwrap
async def add_to_cours(b,message,token_s):
    matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))

    if b.courshandler.load(matiere, token_s[2][0]):
        await b.courshandler.save(matiere, token_s[2][0], message.attachments)
        await message.channel.send("Le fichiers à bien ajoutés aux cours")
    else:
        await message.channel.send("Ce cours n\'existe pas, il est donc impossible d'y ajouter d'autres fichiers. Pour créer un cours utilisez la commande $new-cours")

@commwrap
async def change_cours(b, message, token_s):
    await message.channel.send("Le cours à bien été modifié")

@helpwrap
async def change_cours_h(b, message, token_s):
    await message.channel.send("Besoin d'aide à porpos de la commande change-cours ?")

@commwrap
async def change_dev(b, message, token_s):
    matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))
    nom = token_s[2][0]
    content = token_s[3][0]
    try:
        b.devoirhandler.load(matiere, nom)
        b.devoirhandler.save(matiere, nom, content)
        await message.channel.send("Les devoirs ont bien été modifiés")
    except Exception as e:
        await message.channel.send("Le devoir demandé n\'existe pas, pour créer un devoir utilisez la commande $new-dev")

@helpwrap
async def change_dev_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande change-dev ?")

@commwrap
async def del_cours(b, message, token_s):
    try:
        fichier = token_s[3][0]
        nom = token_s[2][0]
        matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))
        dele = b.courshandler.delete(matiere, nom, fichier)
        if dele:
            await message.channel.send("Ce fichier a été supprimé !")
        else:
            await message.channel.send("Ce fichier n\'a pas été trouvé, réessayez en modifiant l\'orthographe")
    except Exception as e:
        nom = token_s[2][0]
        matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))
        b.courshandler.delete(matiere, nom)
        await message.channel.send("Ce cours a été supprimé !")

@helpwrap
async def del_cours_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande del-cours ?")

@commwrap
async def del_dev(b, message, token_s):
    b.devoirhandler.delete(token_s[1][0], token_s[2][0])
    await message.channel.send("Ce devoir a été supprimé !")

@helpwrap
async def del_dev_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande del-dev ?")

@commwrap
async def get_cours(b, message, token_s):
    matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))
    if len(token_s)>2:
        try:

            file_l = b.courshandler.load(matiere, token_s[2][0])

            await message.channel.send(f"Voici le  Cours intitulé {token_s[2][0]}, Matière : {token_s[1][0]}, Contenu :", files=file_l)
        except Exception as e:
            await message.channel.send("Ce cours n\'existe pas encore, pour créer un cours utilisez la commande $new-cours")
    else:
        dirs_l = b.courshandler.load(matiere)
        mess = f"Voici les cours disponible en {token_s[1][0]} : "
        for i in dirs_l:
            mess += f"\n - \"{i}\" ;"
        mess += f"\n Pour avoir un de ces cours faites: $get-cours \"{token_s[1][0]}\" \"nom du cours\" "
        await message.channel.send(mess)


@helpwrap
async def get_cours_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande get-cours ?")

@commwrap
async def get_dev(b, message, token_s):
    matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))
    dict_data = {}
    try:
        nom = put_in_normes(token_s[2][0])
        dict_data = b.devoirhandler.load(matiere, nom)
        if dict_data =="":
            await message.channel.send("Il n\'y a de devoirs à ce nom, pour créer une liste de devoirs utilisez la commande $new-dev")
        else:
            await message.channel.send(f"\"{nom}\": {dict_data}")

    except Exception as e:
        dict_data = b.devoirhandler.load(matiere)
        end_message = f"`Voici tous les devoirs en {matiere} : `"
        for i in dict_data.keys():
            to_add = f"\n - \"{i}\" : {dict_data[i]}"
            end_message += to_add
        if end_message == f"`Voici tous les devoirs en {matiere} : `":
            end_message = "Il n\'y a rien à faire dans cette matière. Mais vérifie bien l'orhographe dans ta commande au cas où."
        await message.channel.send(end_message)



@helpwrap
async def get_dev_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande get-dev ?")

@commwrap
async def echo(b, message, token_s):
    await message.channel.send(token_s[1][0])

@helpwrap
async def echo_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande echo ?")

@commwrap
async def help(b, message, token_s):
    if len(token_s) == 2:
        try:
            helphandler[token_s[1][0]](b, message, token_s)
        except KeyError:
            pass
    elif len(token_s) == 1:
        try:
            helphandler[token_s[1][0]](b, message, token_s)
        except KeyError:
            pass
    else:
        #illegal argument number
        pass

@helpwrap
async def help_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande help ?")

@commwrap
async def new_dev(b, message, token_s):
    matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))

    date = put_in_normes(token_s[2][0])

    b.devoirhandler.save(matiere, date, token_s[3][0])
    await message.channel.send("Votre devoir a été créé")

@helpwrap
async def new_dev_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande new_dev ?")

@commwrap
async def new_cours(b, message, token_s):
    matiere = '_'.join(find_mat(token_s[1][0].lower()).upper().split('-'))
    await b.courshandler.save(matiere, token_s[2][0], message.attachments)
    await message.channel.send("Votre cours a bien été créé")

@helpwrap
async def new_cours_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande new_cours ?")

@commwrap
async def ping(b, message, token_s):
    await message.channel.send("Eh bah nan!!\nJe t\'ai eu hein?\nChe!!")

@helpwrap
async def ping_h(b, message, token_s):
    await message.channel.send("Besoin d\'aide à propos de la commande ping ?")

@commwrap
async def clear(b, message, token_s):
    if len(token_s) <=2:
        nombre = "10"
        if len(token_s)>1:
            nombre = token_s[1][0].upper()
        print(nombre)
        try:
            await message.channel.purge(limit=int(nombre)+1)
        except Exception as e:
            await message.channel.send("Vous avez mal rentré le nombre de message à supprimer")

    elif len(token_s)>2:
            i = 0
            depart = tri(token_s[1][0], [" ", "\t", "\n"])
            arrivee = tri(token_s[2][0], [" ", "\t", "\n"])
            bracket = False
            sub_b = True
            async for mess in message.channel.history(limit=100):
                if bracket:
                    await mess.delete()
                if str(mess.id) == depart:
                    bracket = sub_b
                    await mess.delete()
                if str(mess.id) == arrivee:
                    if bracket == False:
                        sub_b = False
                        await message.channel.send("Faites attention, vous avez inversé la borne de départ et celle d'arrivée...")
                    else:
                        bracket = False
                        await mess.delete()
                        break

if __name__ == '__main__':
    import Debug
    print(commdict)
    print(helphandler)
    exit(10)
