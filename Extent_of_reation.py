#this program was commented and written in French, you may translate the comments to English.


#On importe les librairies necessaires pour le code

from prettytable import PrettyTable
import matplotlib.pyplot as plot

#On prend les donnes des utilisateurs

Premier_reactif = float(input("Saisi le mol du premier reactif = "))
Deuxieme_reactif = float(input("Saisi le mol du deuxieme reactif = "))
coeff_stocheometriques_du_premier_reactif = float(
    input("Saisi les coeff_stocheometriques correspondants = "))
coeff_stocheometriques_du_deuxieme_reactif = float(
    input("Saisi les coeff_stocheometriques correspondants = "))
coeff_stocheometriques_du_premier_produit = float(
    input("Saisi les coeff_stocheometriques correspondants = "))

#hypothèse 1 : Le Premier reactif est le réactif limitant
xmax_h1=Premier_reactif/coeff_stocheometriques_du_premier_reactif
xmax_h2=Deuxieme_reactif/coeff_stocheometriques_du_deuxieme_reactif 
if xmax_h1<xmax_h2:
    xmax = Premier_reactif / coeff_stocheometriques_du_premier_reactif
    Premier_reactif_final = 0
    Deuxieme_reactif_final = Deuxieme_reactif - coeff_stocheometriques_du_deuxieme_reactif * xmax
    premier_produit_final = coeff_stocheometriques_du_premier_produit * xmax
    print(
      "Le Premier reactif est le réactif limitant"
    )

#hypothèse 2 : Le Deuxieme reactif est le réactif limitant

elif xmax_h2<xmax_h1:
    xmax = Deuxieme_reactif / coeff_stocheometriques_du_deuxieme_reactif
    Premier_reactif_final = Premier_reactif - coeff_stocheometriques_du_premier_reactif * xmax
    Deuxieme_reactif_final = 0
    premier_produit_final = coeff_stocheometriques_du_premier_produit * xmax
    print(
      "Le deuxieme reactif est le réactif limitant"
    )

#Hypthese 3: Cas où les réactifs ont été introduits dans les proportions stoechiométriques

else:
    xmax = Deuxieme_reactif
    Premier_reactif_final = 0
    Deuxieme_reactif_final = 0
    premier_produit_final = coeff_stocheometriques_du_premier_produit * xmax
    print(
        "Les réactifs ont été introduits dans les proportions stoechiométriques"
    )

#On associe ici les nouvelles valeurs au variable qui constitue l'etat intermediaire

Premier_reactif_intermediaire = [Premier_reactif]
Deuxieme_reactif_intermediaire = [Deuxieme_reactif]
premier_produit_intermediaire = [0]
avancement = [0]

#Création d'une variable d'avancement

pas_avancement = 0

#Calcul des quantités de matières pour différentes valeurs d'avancement. Les valeurs calculées sont rajoutées aux listes crées précédemment

while Premier_reactif_intermediaire[-1] > 0 and Deuxieme_reactif_intermediaire[
        -1] > 0:
    pas_avancement = pas_avancement + 0.1
    Premier_reactif_intermediaire.append(
        Premier_reactif -
        coeff_stocheometriques_du_premier_reactif * pas_avancement)
    Deuxieme_reactif_intermediaire.append(
        Deuxieme_reactif -
        coeff_stocheometriques_du_deuxieme_reactif * pas_avancement)
    premier_produit_intermediaire.append(
        0 + coeff_stocheometriques_du_premier_produit * pas_avancement)
    avancement.append(pas_avancement)

#On donne ici la variable "x" la valeur du librairie PrettyTable() pour construire notre tableau d'avancement

x = PrettyTable()

x.field_names = [
    "Tableu d'avancement", "Premier reactif", "Deuxieme reactif ", "Produit"
]

#Nommer les colones et les lignes du tableau

x.add_row(["état initial", Premier_reactif, Deuxieme_reactif, 0])
x.add_row([
    "état intermemediaire",
    str(Premier_reactif) + str("-") +
    str(coeff_stocheometriques_du_premier_reactif) + str("x"),
    str(Deuxieme_reactif) + str("-") +
    str(coeff_stocheometriques_du_deuxieme_reactif) + str("x"),
    str(coeff_stocheometriques_du_premier_produit) + str("x")
])
x.add_row([
    "état final", Premier_reactif_final, Deuxieme_reactif_final,
    premier_produit_final
])
print(x)

#Création du graphique

plot.scatter(avancement, Premier_reactif_intermediaire, marker='+')
plot.scatter(avancement, Deuxieme_reactif_intermediaire, marker='x')
plot.scatter(avancement, premier_produit_intermediaire, marker='o')
plot.title("Evolution des quantités de matière")
plot.xlabel("Avancement x (mol)")
plot.ylabel("Quantités de matières (mol)")

#Choix des valeurs affichées sur le graphique

if Deuxieme_reactif >= Premier_reactif:
    ymax = Deuxieme_reactif

else:
    ymax = Premier_reactif
plot.axis([0, avancement[-1], 0, ymax])

#Affichage du graphique

plot.show()
plot.close()
