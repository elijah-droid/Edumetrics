from django.shortcuts import render, redirect
from .forms import TermForm
from .models import Term

def terms(request):
    return render(request, 'terms.html')

def new_term(request):
    form = TermForm()
    for term in request.user.schooladministrator.current_school.Terms.all():
        for choice in form.fields['Name'].choices:
            try:
                request.user.schooladministrator.current_school.Terms.get(Name__in=choice)
                new_tuple = tuple(filter(lambda x: x != choice, form.fields['Name'].choices))
                form.fields['Name'].choices = new_tuple
            except Term.DoesNotExist:
                pass
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