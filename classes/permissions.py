# ============================================================
# APP : classes
# Fichier : permissions.py (nouveau fichier)
# Rôle : centraliser les règles qui déterminent si un enseignant
#        a le droit de consulter/modifier une classe ou une
#        matière enseignée précise. Sans ça, n'importe quel
#        enseignant connecté pouvait ouvrir la fiche de n'importe
#        quelle classe (et donc voir noms, dates de naissance,
#        contacts de tuteurs...) en changeant juste l'ID dans
#        l'URL — c'est ce trou qu'on corrige ici.
# ============================================================


def enseignant_a_acces_classe(enseignant, classe):
    """
    True si CET enseignant a un lien légitime avec CETTE classe :
    soit il en est l'enseignant principal (titulaire), soit il y
    enseigne au moins une matière (via ClasseMatiere).
    """
    if classe.enseignant_principal_id == enseignant.id:
        return True
    return classe.classematiere_set.filter(enseignant=enseignant).exists()


def enseignant_a_acces_classe_matiere(enseignant, classe_matiere):
    """
    Contrôle plus STRICT que enseignant_a_acces_classe : vérifie
    que l'enseignant est bien celui qui enseigne CETTE matière
    précise, pas seulement qu'il intervient quelque part dans la
    classe. Un professeur de Mathématiques ne doit pas pouvoir
    saisir des notes de Français, même dans une classe où il
    enseigne par ailleurs.

    On garde quand même une exception pour le titulaire de la
    classe (enseignant_principal), qui a un rôle de supervision
    générale — à ajuster si ce n'est pas le comportement voulu
    dans ton établissement.
    """
    if classe_matiere.enseignant_id == enseignant.id:
        return True
    return classe_matiere.classe.enseignant_principal_id == enseignant.id