# ============================================================
# APP : evaluations
# Fichier : forms.py
# Rôle : formulaire de création d'une évaluation (interrogation,
#        devoir, composition).
# ============================================================

from django import forms
from django.forms import inlineformset_factory
from .models import Evaluation, Question, Choix


class EvaluationForm(forms.ModelForm):
    """
    On exclut volontairement 'classe_matiere' : elle est déterminée
    par l'URL (on crée une évaluation DEPUIS la page d'une matière
    enseignée précise), pas choisie dans un menu déroulant — même
    logique que EleveForm dans classes/forms.py.

    On exclut aussi 'est_en_ligne' et 'sequence' pour cette première
    version : ce formulaire couvre les évaluations papier classiques
    (interro, devoir, composition notés à la main). La mise en ligne
    pour les élèves (QCM) sera un formulaire séparé, plus tard.
    """

    class Meta:
        model = Evaluation
        fields = [
            'titre',
            'type_evaluation',
            'trimestre',
            'bareme_total',
            'coefficient',
            'date_evaluation',
        ]
        widgets = {
            'date_evaluation': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class QuestionForm(forms.ModelForm):
    """
    Informations d'UNE question (énoncé, type, points). Les choix
    de réponse (si type_question='QCM') sont gérés séparément par
    ChoixFormSet, une fois la question déjà créée — même logique en
    deux temps que FichePreparation/EtapeFiche dans l'app pedagogie.
    """

    class Meta:
        model = Question
        fields = ['numero_ordre', 'enonce', 'type_question', 'points']
        widgets = {
            'enonce': forms.Textarea(attrs={'rows': 2}),
        }


# ChoixFormSet : 4 propositions vides par défaut (1 bonne réponse +
# 3 distracteurs, le format QCM le plus courant), modifiable par
# l'enseignant (ajout/suppression de lignes via can_delete).
ChoixFormSet = inlineformset_factory(
    Question,
    Choix,
    fields=['texte', 'est_correct'],
    extra=4,
    can_delete=True,
)