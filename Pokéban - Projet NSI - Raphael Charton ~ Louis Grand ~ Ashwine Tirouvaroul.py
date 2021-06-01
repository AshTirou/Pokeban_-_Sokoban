
"""POKEBAN (SOKOBAN) - Raphael CHARTON ~ Louis GRAND ~ Ashwine TIROUVAROUL - 2021"""
## https://github.com/PeppAshPig/Pokeban_-_Sokoban

#Les polices du jeu sont contenues dans le dossier 'font' sous le format .tff
#Les images sont contenues dans le dossier 'Img' de type PNG ou JPG déjà redimensionnées
### Utilisez CTRL + ALT afin de sélectionner votre niveau en l'entrant sur le Pavé Numérique

'''MODULES'''

"""folder.file correspond au fichier "file.py" contenu dans le dossier "folder" """
from module_map.graphic_mansart_modified import*
## Utilisation des fonctions : aff_pol_2 / load_image_2 / chrono_start() / chrono_val
from random import*
## Utilisation de la fonction : randint
from copy import*
## Utilisation de la fonction : deepcopy
from module_map.map_levels import*
## Utilisation des variables contenants les maps (CONTIENT LÉGENDE DES CARACTÈRES)


'''FONCTIONS'''

def touche_selec():
    """ Fonction adaptée de wait_arrow() de graphic_mansart
    Attend que l'on presse une touche du clavier.
    Renvoie "up", "down", "left", "right", "escape", "enter" ou "TAB"
    suivant que l'on a tapé sur la flèche du haut, du bas, de gauche ou de droite,
    ou la touche échap, entrée ou tabulation.
    La combinaison CTRL + ALT renvoie 'hack'.
    Renvoie une chaîne vide sinon.
    Instruction bloquante.
    """
    if PYGAME_SDL_AFFICHAGE == 1 :
        affiche_all()

    pygame.event.clear()

    while 1 :
        for event in pygame.event.get() :
            if event.type == KEYDOWN:
                if event.key == K_UP :
                    return "up"
                elif event.key == K_DOWN :
                    return "down"
                elif event.key == K_LEFT :
                    return "left"
                elif event.key == K_RIGHT :
                    return "right"
                elif event.key == K_ESCAPE :
                    return "escape"
                elif event.key == K_RETURN or event.key == K_KP_ENTER:
                    return "enter"
                elif event.key == K_TAB:
                    return "TAB"
                elif event.mod & pygame.KMOD_CTRL or event.mod & KMOD_ALT:
                    if event.key == K_LCTRL or event.key == K_RCTRL or event.key == K_LALT :
                        return("hack")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def chargement_map():
    """Cette fonction permet de recharger le fond/décor de la map"""
    for i in range(10):
        for k in range (10):
            load_image_2("Img/fougeres2.png",75*i,75+75*k)



    nombre_sala = randint(1,7)
    nombre_sala2 = randint(1,7)

    load_image_2("Img/bassin2.png",75*8,75)

    load_image_2("Img/salameche2.png",75*nombre_sala2,75*nombre_sala)
    load_image_2("Img/fleur2.png",0,75)
    load_image_2("Img/fleur2.png",0,0)
    load_image_2("Img/fleur2.png",675,0)
    load_image_2('Img/fleur2.png',75*6,75*7)
    nombre = randint(6,8)
    nombre2 = randint(0,9)
    load_image_2('Img/fleur2.png',75*nombre2,75*nombre)
    nombre = randint(6,8)
    nombre2 = randint(0,9)
    load_image_2('Img/fleur_jaune2.png',75*nombre2,75*nombre)
    load_image_2('Img/pika-sacha2.jpg',75,0)
    aff_pol_2("nb coups : ",15,110,50,pygame.Color(255,0,0),text_bold=True,text_italic=True)
    aff_pol_2("Timer :",15,275,50,pygame.Color(255,0,0),text_bold=True,text_italic=True)
    aff_pol_2("Level :",25,180,10,pygame.Color(255,0,0),text_bold=True,text_italic=False)

    load_image_2("Img/chemin2.png",0,75*8)
    for i in range(10):
        load_image_2("Img/barriere2.png",0+75*i,75*9)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def changement(list):
    """Cette fonction prend en argument une liste de liste composée de X listes
    composées chacune de 8 caractères chacunes.
    Elle permet de transfomrmer la liste composée de caractères en une image déjà
    redimensionée (75px,75px) sur la fenêtre graphique
    Cf. Légende des caractères dans le fichier module_map/map_levels.py
    """
    global sacha2,nombre_sala,nombre_sala2,nb_mouv
    for a in range (len(list)):
        for b in range(7):
            if list[a][b]== "#":
                load_image_2("Img/buisson2.png",75 + 75*b,75+75*a)
            if list[a][b]== "$":
                load_image_2("Img/pikachu2.png",75 + 75*b,75+75*a)
            if list[a][b]== "@":
                load_image_2(sacha2,75+75*b,75+75*a)
            if list[a][b]== " ":
                load_image_2("Img/fond_vert2.png",75+75*b,75+75*a)
            if list[a][b]== ".":
                load_image_2("Img/pokeball_ouverte2.png",75+75*b,75+75*a)
            if list[a][b]== "*":
                load_image_2("Img/pokeball_ferme2.png",75+75*b,75+75*a)

    #Affiche une image par dessus le Timer et nb coups pour qu'il soit lisible
    load_image_2("Img/fond_vert_yolo2.png",205,50)
    load_image_2("Img/fond_vert_yolo2.png",205+25,50)
    load_image_2("Img/fond_vert_yolo2.png",337,50)
    load_image_2("Img/fond_vert_yolo2.png",362,50)
    aff_pol_2(str(nb_mouv),20,205,50,pygame.Color(255,0,0),text_bold=True,text_italic=True)
    aff_pol_2(str(int(chrono_val()/1000)),20,337,50,pygame.Color(255,0,0),text_bold=True,text_italic=True)

    """Louis et Ashwine n'étant pas d'accord sur le fait que les buissons soient sur le chemin
    Alors c'est une valeur aléatoire qui va choisir... (Ex : Level 52)
    """
    val_aléa = randint(0,1)
    if val_aléa == 0 :
        load_image_2("Img/chemin2.png",0,75*8)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main(Level, Level_modif,Level_destination):
    """
    La fonction main possède la logique du Sokoban (Condition, déplacement, vérification de victoire)
    Coordonnées = Indice dans la liste de liste soit [y,x]
    Il prend en arg Level qui est la map "référente" qui ne change pas
    Level_modif est l'identique mais celui-ci sera modifiée
    Level_destination est une liste de liste composée des coordonnées des destinations finales
    Selon les touches appuyées :
        Flèches directionnelles : Level_modif/Map est modifiée
        Tabulation : Renvoie "False" - Recommence le niveau en cours
        Entrée : Renvoie "True" - Passe au niveau prochain (si gagné)
        Echap : Ferme interface Pygame et Python
    """
    #Chaine contiendra la position du joueur (coordonnées)
    chaine = ""
    global sacha2,nb_mouv
    #Détermine la position du joueur dans la map référente
    for i in range(len(Level)):
        for j in range(len(Level[i])):
            if Level[i][j] == "@":
                chaine =  i,j
    ##------------------------------------------------------------------------------------------------------------------------------------------------------------------##
    while True:

        """
        Les déplacements du joueur/des caisses sont basés sur la logique des listes de listes
        S'il se déplace verticalement, alors on passe d'une liste à une autre
        Un déplacement horizontal, restera sur la même liste, mais changera de position dans celle-ci
        Ainsi selon le déplacement voulu, l'une des deux variables (direction_chiffre_verticale et
        direction_chiffre_horizontale), se verra attribuer une valeur
        -1 : Haut / 1 : Bas / -1 : Gauche / Droite : 1
        Dépend du sens de déplacement dans la liste
        """
        direction_chiffre_verticale = 0
        direction_chiffre_horizontale = 0

        #Boucle pour la sélection de la touche, évite consommation du code en cas de touche erronée
        while True:

            #On récupère la touche appuyée dans direction
            direction = touche_selec()

            #Si échap quitte pygame et arrête le programme
            if direction == "escape":
                shutdown()

            #Si tabulation renvoie False, cf Partie "Programme" (variable valid)
            elif direction == "TAB":
                return False

           #Si touche directionelle appuyée
            elif direction == "up" or direction == "down" or direction == 'left' or direction == "right":

                nb_mouv +=1

                if direction == "up" :
                    sacha2="Img/sacha_dos2.png"
                    direction_chiffre_verticale = -1
                elif direction == "down":
                    direction_chiffre_verticale = 1
                    sacha2 ="Img/sacha_face2.png"

                elif direction == 'left':
                    sacha2="Img/sacha_cote_gauche2.png"
                    direction_chiffre_horizontale = -1
                elif direction == 'right':
                    sacha2 ="Img/sacha_cote_droit2.png"
                    direction_chiffre_horizontale = 1

                #Permet de briser la boucle While True pour la sélection de la touche
                break

        ##------------------------------------------------------------------------------------------------------------------------------------------------------------------##

        """pass permet de passer toutes les conditions qui suit (ne sont pas traitées)"""
        #On retire 1 au nb de mouvement si rien ne se passe (pass)
        if Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] == '#':
            '''Vérifie s'il y a un mur'''
            nb_mouv -= 1
            pass


        elif Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] == '.':
            '''Vérifie si c'est une destination'''
            Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] = '@'
            Level_modif[chaine[0]][chaine[1]] = ' '


        elif Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] == '$' or Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] == '*':
            '''Vérifie s'il y a Pikachu (Dans Pokéball ou non)'''
            if Level_modif[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] == '#':
                '''Vérifie s'il y a un mur derrière Pikachu'''
                nb_mouv -= 1
                pass
            elif Level_modif[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] == '$' or Level_modif[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] == '*':
                '''Vérifie s'il y a un autre Pikachu derrière ce Pikachu'''
                nb_mouv -= 1
                pass
            else:
                if Level[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] == '.' or Level[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] == '*':
                    '''Vérifie si c'est une destination'''
                    Level_modif[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] = "*"
                    Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] = "@"
                    Level_modif[chaine[0]][chaine[1]] = " "
                else:
                    '''Déplace le joueur et Pikachu si aucune des conditions contraignantes sont présentes'''
                    Level_modif[chaine[0]+direction_chiffre_verticale*2][chaine[1]+direction_chiffre_horizontale*2] = "$"
                    Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] = "@"
                    Level_modif[chaine[0]][chaine[1]] = " "

        else:
            '''Déplace seulement le joueur s'il n'y a ni Pikachu et aucune conditions contraignantes présentes'''
            Level_modif[chaine[0]][chaine[1]], Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale] = Level_modif[chaine[0]+direction_chiffre_verticale][chaine[1]+direction_chiffre_horizontale], Level_modif[chaine[0]][chaine[1]]
        ##------------------------------------------------------------------------------------------------------------------------------------------------------------------##
        #Détermine à nouveau la position du joueur dans la map modifiée
        for i in range(len(Level_modif)):
            for j in range(len(Level_modif[i])):
                if Level_modif[i][j] == "@":
                    chaine = i,j
        ##------------------------------------------------------------------------------------------------------------------------------------------------------------------##
        #Vérifie que les emplacements destinés ne sont pas vides grace aux coordonnées de Level_destination, si oui, ajoute de nouveau le point
        for i in Level_destination:
            if Level_modif[i[0]][i[1]]==" ":
                Level_modif[i[0]][i[1]] = '.'
        ##------------------------------------------------------------------------------------------------------------------------------------------------------------------##
        #Actualise la map modifiée sur l'interface graphique
        changement(Level_modif)
        ##------------------------------------------------------------------------------------------------------------------------------------------------------------------##
        '''VERIFIE SI GAGNÉ'''

        #Compte le nb de Pikachu dans sa Pokéball
        count = 0
        for i in Level_destination:
            if Level_modif[i[0]][i[1]]=="*":
                count += 1

        #Si nb de Pikachu dans sa Pokéball correspond au nb de destination, alors GAGNÉ
        if count == len(Level_destination):

            #Permet l'acutalisation de la fenêtre avant le delay afin d'éviter un gêle de l'écran
            pygame.display.flip()
            pygame.time.delay(250)
            draw_fill_rectangle_2(750/2,750/2-39,410,410,pygame.Color(0,0,0))
            draw_rectangle_2(750/2,750/2-39,400,400,pygame.Color(0,0,0))
            load_image_2('Img/gagne2.png',175,137)

            #Boucle pour la sélection de la touche, évite autres touches
            while True:
                key = touche_selec()
                if key == 'enter':
                    chargement_map()
                    return True
                elif key == "TAB":
                    return False
                elif key == 'escape':
                    shutdown()

def shutdown():
    """ Permet la fermeture de la fenêtre graphique et l'arrêt total du programme
    exit() permet l'arrêt total du code, évite les erreurs de code après pygame.quit()
    """
    pygame.quit()
    exit()

'''PROGRAMME PRINCIPAL'''

#Change la police, importé depuis le fichier Pokemon Hollow.tff
change_font("font/Pokemon Hollow.ttf")

#______________## INITIALISATION FENETRE GRAPHIQUE ##______________#

""""initialisation de la fenêtre des règles au début du jeu """
x=0
while x<1:
    if x==0:
        init_graphic(750,750,name="Pokéban",bg_color=pygame.Color(206,206,206),fullscreen=0)

        #Affiche l'image de fond du MENU et le nom Pokéban, modifié la police pour la partie "règles"
        load_image_2("Img/regles_poke2.png",0,0)
        aff_pol_2("Pokéban ",70,750/2,10,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        change_font("font/Bauhaus 93 Regular.ttf")

        #Règles du jeu
        aff_pol_2("Le but du jeu est de pousser ",30,315,120,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2(" Pikachu dans sa Pokéball: ",30,330,150,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2("1 : Vous ne pouvez pas tirer Pikachu ",20,370,220,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2("          seulement le pousser ",20,380,260,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2("2 : ",20,390,290,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2("3 :  'Échap'   ->  Quitter  ",20,390,490,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2("4 :  'TAB'   ->   Recommencer  ",20,370,530,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2("5 : 'Entrée   ->   Niveau suivant",20,340,570,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        load_image_2("Img/bouton_regles2.png",450,310)
        aff_pol_2("6 : Appuyez sur 'Entree' lorsque vous avez ",20,310,610,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2(" fini de lire les consignes",20,360,640,pygame.Color(255,255,255),text_bold=True,text_italic=True)
        aff_pol_2(" Bon courage !",25,55,595,pygame.Color(0,0,0),text_bold=True,text_italic=True)
        aff_pol_2(" vous en aurez besoin.....",17,530,695,pygame.Color(255,255,255),text_bold=True,text_italic=True)

        #Récupère la touche sélectionnée
        key = touche_selec()

        #Récupère la touche sélectionnée pour quitter le menu
        if key == 'enter' or key =='right' or key == 'left' or key == 'up' or key == 'down':
            #Quitte la boucle While si Entrée ou touches directionnelles appuyées
            x=1

        elif key == "hack":
            '''Permet de sélectionner le niveau voulu'''
            #On utilise les event pygame pour récupérer les numéros (chaine de caractère)
            level_demandé_input = ''
            #Les deux boucles while fonctionnent grace à x afin de ne modifier qu'une seule valeur lors de la sortie de la boucle
            while x == 0 :
                for event in pygame.event.get() :
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            #Fermer la fenêtre graphique
                            shutdown()
                        elif event.key == K_RETURN or event.key == K_KP_ENTER:
                            #Si 'Entrée' est appuyée alors la valeur indiquée est prise en compte, on sort de la boucle
                            x = 1
                            break
                        elif event.key == K_BACKSPACE:
                            #Permet de retirer le dernièr caractère entrée dans la chaine de caractère
                            level_demandé_input = level_demandé_input[:-1]
                        else :
                            #On ajoute à la chaine de caractère la touche pressé en unicode
                            level_demandé_input += event.unicode
                        #On trace un carré de fond noir sur lequel on affiche ce que l'utilisateur a écrit
                        draw_fill_rectangle_2(750/2,750/2,750,750,pygame.Color(0,0,0))
                        aff_pol_2("Le Niveau voulu est le : " + level_demandé_input,50,75,750/2-50,pygame.Color(255,255,255),text_bold=True)
                        #Actualise la fenêtre graphique
                        pygame.display.update()

        elif key == 'escape':
            #Ferme la fenêtre graphique
            shutdown()


#______________## PROGRAMME ##______________#

#La police du jeu est Pokemon Solid
change_font("font/Pokemon Solid.ttf")

'''Les maps sont contenues dans le ficier module_map/map_levels.py'''

#MAX_LEVEL_INDEX est le nombre de level maximum existant
MAX_LEVEL_INDEX = len(level_list)-1
#Vérifie si level_demandé_input existe ou si level_demandé est convertissable en entier, si non, le niveau du début est 0
if 'level_demandé_input' not in locals() or level_demandé_input.isdigit() == False:
    niveau_en_cours = 0

else:
    #Si la map demandée est supérieure au nb de level maxi, elle est assignée au level max existant
    if int(level_demandé_input) > MAX_LEVEL_INDEX:
        level_demandé_input = MAX_LEVEL_INDEX
    #Assigne la map de départ à celle demandée ou au Maxi
    niveau_en_cours = int(level_demandé_input)


while niveau_en_cours <= MAX_LEVEL_INDEX:
    """
    La variable valid va nous permettre de recommencer le niveau si besoin
    Ainsi si la fonction principale retourne False (touche : TAB), on va recommencer le niveau
    Lorsque le niveau sera gagné, il retournera True afin de passer au niveau suivant
    """
    valid = None

    while valid == None :

        '''On initiliase tout (interface graphique et variables), puis la fonction principale est éxécutée'''
        chargement_map() #Décor
        chrono_start() #Lancement du chrono
        nb_mouv=0 #Nombre de déplacement définit à zéro
        sacha2= "Img/sacha_face2.png" #La position de sacha est définit de face
        aff_pol_2(str(niveau_en_cours),25,280,10,pygame.Color(255,0,0),text_bold=True,text_italic=False) #On affiche le niveau en cours

        changement(level_list[niveau_en_cours][1]) #On actualise la page avec la map
        valid = main(level_list[niveau_en_cours][0],level_list[niveau_en_cours][1],level_list[niveau_en_cours][2]) #Exécute la fonction principale

        if valid == False:
            """deepcopy va nous permettre la copie de la liste (map référent)
            Sur celles en cours sans lien entre elles. Utilise la bilbiothèque copy"""
            level_list[niveau_en_cours][1] = deepcopy(level_list[niveau_en_cours][0])

            #valid devient de nouveau None afin de rester dans la boucle tant qu'elle est égale à True
            valid = None

    niveau_en_cours+=1
    #Si tous les niveaux sont finis alors le jeu se ferme
    if niveau_en_cours > MAX_LEVEL_INDEX:
        shutdown()


"""POKEBAN (SOKOBAN) - Raphael CHARTON ~ Louis GRAND ~ Ashwine TIROUVAROUL - 2021"""
