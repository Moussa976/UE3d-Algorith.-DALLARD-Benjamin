# 1) Simple échange A=>B et B=>A
A = 5; B=3;
C = A;
A = B;
B = C;
// affiche A et B
# 2) Demandez un nombre à un utilisateur et afficher le carré
Saisir n;
A = n**2;
// affiche A;
# 3) Demandez un nombre à un utilisateur et afficher s’il est positif ou négatif.
Saisir n;
si n > 0 alors
  // affiche "positif"
sinon 
  // affiche "négatif"
# 4) Demandez à un utilisateur deux nombres, et indiquez si le produit est négatif ou positif (zéro est positif) SANS FAIRE LA MULTIPLICATION
Saisir n1; n2;
si n1 >= 0 et n2 >= 0
  // affiche "positif"
sinon 
  // affiche "négatif"
# 5) Ecrivez un algo qui à partir d’un nombre de départ, va afficher les dix suivants
Saisir n;
B = n+10;
for i in range(n,B)
  #affiche i
# 6) A partir d’un nombre (positif) donné la somme de tous les entiers jusqu’à ce nombre
Saisir n;
LasommeDu_n = 0;
for i in range(1,n)
  LasommeDu_n = LasommeDu_n + i;
fin for
// affiche LasommeDu_n
---
 
 
