from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Task
from .forms import TaskForm

"""
Etant donné que base.html donne ma mise en page, task_list et task_detail doivent aussi etre affiché. 
Une vue fait le lien entre le modèle (données) et le template (affichage). task_list.html ou task_detail.html
héritent de base.html. Même si task_list.html hérite de base.html, le template a besoin qu’on lui donne les données.

"""

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})
"""
L’utilisateur doit voir un formulaire vide pour remplir titre, description, date, 
Quand il clique sur “Créer”, le site doit prendre les informations, vérifier si elles sont valides, et enregistrer la
 nouvelle tâche dans la base.
Ensuite, l’utilisateur doit recevoir un message de confirmation (“Task created”) et être redirigé vers la liste des tâches.
On veut que l’utilisateur puisse modifier , supprimer une tâche existante.
’utilisateur doit voir le formulaire rempli avec les infos actuelles de la tâche. L’utilisateur doit recevoir un message de 
confirmation et être redirigé vers la page des détails de la tâche.
"""
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created.")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'create': True})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated.")
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'task': task, 'create': False})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted.")
        return redirect('task_list')
    # If your delete confirmation is in template, render it on GET
    return render(request, 'task_confirm_delete.html', {'task': task})


"""
Nous voulons mettre en place application de liste de tâches (to-do app). Chaque tâche a une petite case à cocher à côté pour indiquer si elle est faite ou non.
La fonction task_toggle est la partie de  Django qui change l’état de cette case.
C’est-à-dire qu’elle fait passer la tâche : “non terminée”  à “terminée” et vice-versa
Affiche une liste de tâches avec des boutons (“Marquer comme terminée” / “Marquer comme non terminée”).
Quand l’utilisateur clique sur ce bouton, l’application change l’état de la tâche tout de suite.
Après ce changement, l’application affiche un petit message (“Tâche marquée comme terminée”) et revient à la liste.
On veut que notre application permette à l’utilisateur de marquer une tâche comme faite ou non faite en un seul clic  sans passer par la page d’édition.
Mais je ne voudrais  pas que l’utilisateur doive ouvrir un long formulaire juste pour cocher une case ou 
qu’il doive recharger la page ou ressaisir des données.

"""

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    messages.success(request, f"Task marked {'complete' if task.completed else 'incomplete'}.")
    next_url = request.GET.get('next') or reverse('task_list')
    return redirect(next_url)

