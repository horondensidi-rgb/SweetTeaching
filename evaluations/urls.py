# ============================================================
# APP : evaluations
# Fichier : urls.py (à créer, n'existe pas encore)
# ============================================================

from django.urls import path
from . import views

app_name = 'evaluations'

urlpatterns = [
    path(
        'classe-matiere/<int:classe_matiere_id>/',
        views.liste_evaluations_view,
        name='liste_evaluations'
    ),
    path(
        'classe-matiere/<int:classe_matiere_id>/creer/',
        views.creer_evaluation_view,
        name='creer_evaluation'
    ),
    path(
        '<int:evaluation_id>/notes/',
        views.saisir_notes_view,
        name='saisir_notes'
    ),
    path(
        '<int:evaluation_id>/modifier/',
        views.modifier_evaluation_view,
        name='modifier_evaluation'
    ),
    path(
        '<int:evaluation_id>/supprimer/',
        views.supprimer_evaluation_view,
        name='supprimer_evaluation'
    ),
    path(
        '<int:evaluation_id>/questions/',
        views.liste_questions_view,
        name='liste_questions'
    ),
    path(
        '<int:evaluation_id>/questions/creer/',
        views.creer_question_view,
        name='creer_question'
    ),
    path(
        'questions/<int:question_id>/modifier/',
        views.modifier_question_view,
        name='modifier_question'
    ),
    path(
        'questions/<int:question_id>/choix/',
        views.modifier_choix_view,
        name='modifier_choix'
    ),
    path(
        'questions/<int:question_id>/supprimer/',
        views.supprimer_question_view,
        name='supprimer_question'
    ),
]
