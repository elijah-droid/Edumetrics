from django.shortcuts import render
from .models import PastPaper
from .forms import PastPaperForm


def parent_view_pastpapers(request):
    form = PastPaperForm()
    context = {
        'form': form
    }
    return render(request, 'parent_pastpapers.html', context)
