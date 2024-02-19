class Livre:
    def __init__(self, p_titre: str = "", p_prix: float = 0.0):
        self.titre = p_titre
        self.prix = p_prix


class Gateau:
    # Attribut de classe
    saveur = "Chocolat"
    # Liste des instances Gateau
    lst_gateau = []

    def __init__(self, p_quantite: int = 0, p_prix: float = 0.0):
        self.quantite = p_quantite
        self.prix = p_prix
        Gateau.lst_gateau.append(self)

    def __str__(self):
        return ("La quantité du gâteau est de: " + str(self.quantite) +
                "\nLe prix du gâteau est de: " + str(self.prix))

    def __add__(self, p_gateau):
        return self.prix + p_gateau.prix

    def __len__(self):
        return self.quantite

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

    @staticmethod
    def comparer_prix(gat1, gat2):
        if gat1.prix > gat2.prix:
            return gat1
        else:
            return gat2


gateau1 = Gateau()
gateau1.prix = 10
gateau2 = Gateau()
gateau2.prix = 20
print(Gateau.comparer_prix(gateau1, gateau2))   # Comparer qté
print(gateau1 + gateau2)    # @classmethod
gateau1.quantite = 100
print(len(gateau1))     # @staticmethod
print(Gateau.lst_gateau)

# gateau1 = Gateau()
# print(gateau1.saveur)
# print(gateau1.retourner_saveur())
#
# gateau2 = Gateau()
# print(gateau2.saveur)
# print(gateau2.retourner_saveur())
# gateau2.saveur = "Fraise"
# print(gateau2.saveur)
#
# print(Gateau.saveur)
#
# gateau1.quantite = 5
# gateau2.quantite = 10
#
# print(gateau1.quantite)
#
# gateau1.comparer_quantite(gateau2)


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
