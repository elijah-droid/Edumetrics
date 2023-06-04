from django.shortcuts import render, redirect
from .forms import AdmissionForm
from django.core.mail import send_mail

def admissions(request):
    return render(request, 'admissions.html')

def admit(request):
    form = AdmissionForm()
    form.fields['Student'].queryset = request.user.schooladministrator.current_school.students.all()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        admission = form.save(commit=False)
        admission.Examined_By = request.user.schooladministrator
        admission.save()
        request.user.schooladministrator.current_school.patient_admissions.add(admission)
        send_mail(
            f'{admission.Student} has been examined by {request.user.schooladministrator} and is found to be sick.',
            admission.Complications,
            'edumetrics@sparklehandscs.com',
            [parent.user.email for parent in admission.Student.parents.all()]
        )
        return redirect('admissions')
    else:
        return render(request, 'admit.html', context)


def dismiss(request):
    pass