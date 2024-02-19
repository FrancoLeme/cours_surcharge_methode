class Livre:
    def __init__(self, p_titre: str = "", p_prix: float = 0.0):
        self.titre = p_titre
        self.prix = p_prix


class Gateau:
    # Attribut de classe
    saveur = "Chocolat"

    def __init__(self, p_quantite: int = 0):
        self.quantite = p_quantite

    def __str__(self):
        return "La quantité du gâteau est de:", str(self.quantite)

    def comparer_quantite(self, p_gateau):
        """

        :param p_gateau:
        :return:
        """
        if self.quantite > p_gateau.quantite:
            return self
        else:
            return p_gateau


    @classmethod
    def retourner_saveur(cls):
        return cls.saveur


gateau1 = Gateau()
print(gateau1.saveur)
print(gateau1.retourner_saveur())

gateau2 = Gateau()
print(gateau2.saveur)
print(gateau2.retourner_saveur())
gateau2.saveur = "Fraise"
print(gateau2.saveur)

print(Gateau.saveur)

gateau1.quantite = 5
gateau2.quantite = 10

print(gateau1.quantite)

gateau1.comparer_quantite(gateau2)

# livre1 = Livre("l'alchimiste", 20)    ctr + / pour mettre en commentaire
# print(livre1.prix)
#
# livre2 = Livre()
# print(livre2.prix)
#
# livre3 = Livre("Python pour les nuls")
# print(livre3.prix)
#
# livre4 = Livre(p_prix=20.5)
# print(livre4.prix)
