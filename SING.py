# -*- coding: utf-8 -*-
"""
Author: Kombila Mamboundou Joel
Function: check if an article is positiv or not
"""
import codecs 
import requests
from urllib.parse import urlparse
from urllib import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMB


#get an url html thanks to urlib
def enregistrerArticle(url):
    if(url==""):
        var = StringVar()
        label = Label( jeu, textvariable=var )
        var.set("Entrer un lien")
        label.pack()
    o = urlparse(url)
    r = requests.get(o.geturl())
    with open('article/ article.txt', 'w', encoding='utf-8') as file:
        file.write(r.text)
    file.close()
#compare the html with the dictionnary
def comparerDico():
    fichier = open('dico/positif.txt','r')
    contenu=fichier.read()
    dico=contenu.split(",")
    fichier.close()
    file = codecs.open("article/article.txt", "r", "utf-8")
    article=file.read()
    rec=0
    for i in range(len(dico)):
        if(dico[i] in article):
            rec=rec+1
    if rec >=20:
        var = StringVar()
        label = Label( jeu, textvariable=var )
        var.set("L'article est positif")
        label.pack()
    elif  ((rec<20) and (rec>5)):
        var = StringVar()
        label = Label( jeu, textvariable=var )
        var.set("L'article est neutre")
        label.pack()
    elif  (rec<=5):
        var = StringVar()
        label = Label( jeu, textvariable=var )
        var.set("L'article est négatif")
        label.pack()   
#main function
def use():
    global entree
    url = entree.get()
    enregistrerArticle(url)
    comparerDico()
#creation de la fenetre 
jeu = Tk()
cadre = Frame(jeu)
cadre.pack(padx=20, pady=20)
# Titre (Label)
titre = Label(jeu, text = "Entrez l'url d'un article")

# Affichage du titre
titre.pack(padx=5, pady=5, side=TOP)
etiquette = Label(cadre, text='Url :')
etiquette.pack(padx=5, pady=5, side=LEFT)

#label entry
entree = Entry(cadre, width=50)
entree.pack(padx=5, pady=5, side=LEFT)
entree.focus_force()
#utiliser la fonction
btnAffiche = Button(jeu, text='Entrer', command=use)
btnAffiche.pack(padx=5, pady=5)
jeu.mainloop() 