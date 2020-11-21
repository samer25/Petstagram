from django.shortcuts import render, redirect

# Create your views here.
from pets.forms import CreateForm, CommentForm
from pets.models import Pet, Like, Comments


def list_pets(req):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(req, 'pets/list_pets.html', context)


def show_pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    context = {
        'pet': pet,
        'form': CommentForm(),
        'comments': Comments.objects.all(),
    }
    if req.method == 'GET':
        return render(req, 'pets/details_pets.html', context)
    else:
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = Comments(comment=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details', pet.pk)


def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(like_id=pk)
    like.pet = pet
    like.save()
    return redirect('list pet')


def create(req):
    if req.method == 'GET':
        form = CreateForm()
        return render(req, 'pets/pet_create.html', {'form': form})
    else:
        form = CreateForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('list pet')
        return render(req, 'pets/pet_create.html', {'form': form})


def edit(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == 'GET':
        form = CreateForm(instance=pet)
        return render(req, 'pets/pet_edit.html', {'form': form})
    else:
        form = CreateForm(req.POST, req.FILES,  instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', pk)
        return render(req, 'pets/pet_edit.html', {'form': form})


def delete_pet(req, pk):
    context = {
        'pet': Pet.objects.get(pk=pk),

    }
    if req.method == 'GET':
        return render(req, 'pets/pet_delete.html', context)
    else:
        context['pet'].delete()
        return redirect('list pet')
