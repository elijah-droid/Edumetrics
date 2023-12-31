from django.shortcuts import render, redirect
from .models import PastPaper
from Examinations.forms import PaperForm
from .forms import PastPaperForm
from Examinations.models import Paper
from django.core.paginator import Paginator
import os
from django.http import FileResponse


def browse_pastpapers(request):
    form = PaperForm()
    del form.fields['Date']
    del form.fields['Time']
    del form.fields['Examiner']
    del form.fields['Duration']
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PastPaperForm(request.POST)
        del form.fields['Questions_Pdf']
        del form.fields['Answers_Pdf']
        del form.fields['Description']
        del form.fields['Price']
        if form.is_valid():
            parameters = form.cleaned_data
            pastpapers = PastPaper.objects.filter(Class=parameters['Class'], Subject=parameters['Subject'])
            paginator = Paginator(pastpapers, 12)
            page = request.GET.get('page')
            papers = paginator.get_page(page)
            context = {
                'papers': papers
            }
            return render(request, 'query_results.html', context)
    else:
        return render(request, 'browse_pastpapers.html', context)


def teachers_pastpapers(request):
    paginator = Paginator(request.user.teacher.Past_Papers.all(), 12)
    page = request.GET.get('page')
    papers = paginator.get_page(page)
    context = {
        'papers': papers
    }
    return render(request, 'teacher_pastpapers.html', context)

def upload_pastpaper(request):
    form = PastPaperForm()
    form.fields['Paper'].queryset = Paper.objects.filter(Examiner=request.user.teacher, Paper=None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PastPaperForm(request.POST, request.FILES)
        if form.is_valid():
            pastpaper = form.save()
            pastpaper.Paper.Paper = pastpaper
            pastpaper.Paper.save()
            request.user.teacher.Past_Papers.add(pastpaper)
            return redirect('pastpapers')
    else:
        return render(request, 'upload_pastpaper.html', context)


def download_pastpaper(request, paper):
    paper = PastPaper.objects.get(id=paper)
    file = open(paper.Questions_Pdf.path, 'rb')
    return FileResponse(file, as_attachment=True)


def delete_paper(request, paper):
    paper = Paper.objects.get(id=paper)
    paper.delete()
    return redirect('pastpapers')