from django.shortcuts import render, redirect
from .forms import LanguageForm, FrameworkForm
from .models import Language, Framework


# Create your views here.
def index(request):
    return render(request, 'bsapp/index.html', {})


def add_language(request):
    form = LanguageForm(request.POST or None)
    if form.is_valid():
        # form.save()
        language_obj = Language(name=form.cleaned_data['name'])
        language_obj.save()
        return redirect('bsapp:index')
    return render(request, 'bsapp/add_language.html', {'form': form})


def add_framework(request):
    form = FrameworkForm(request.POST or None)
    if form.is_valid():
        # form.save()
        framework_obj = Framework(
            name=form.cleaned_data['name'],
            language=form.cleaned_data['language']
        )
        framework_obj.save()
        return redirect('bsapp:index')
    return render(request, 'bsapp/add_framework.html', {'form': form})
