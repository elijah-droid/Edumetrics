from django.shortcuts import render, redirect
from .forms import TermForm
from .models import Term

def terms(request):
    return render(request, 'terms.html')

def new_term(request):
    form = TermForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid:
            term = form.save(commit=False)
            term.School = request.user.schooladministrator.current_school
            term.save()
            term.School.Terms.add(term)
            return redirect('terms')
    else:
        return render(request, 'new_term.html', context)


def switch_term(request, term):
    term = Term.objects.get(pk=term)
    request.user.schooladministrator.current_school.current_term = term
    request.user.schooladministrator.current_school.save()
    recent_url = request.META.get('HTTP_REFERER')
    return redirect(recent_url)