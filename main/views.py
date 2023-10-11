from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import patient as P
from .models import ward as W
from django.urls import reverse
from .forms import PatientForm
from django.db.models import Q



# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        #data = P.objects.filter(name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q( initials__icontains=q) | Q(ward_id=q))
        data = P.objects.filter(multiple_q)
    else:
        data= P.objects.all()
    return render(request,'index.html',{
        'patients':data
        })

def view_patient(request,id):
    return HttpResponseRedirect(reverse('index'))

def wards(request):
    return render(request,'wards.html',{'wards':W.objects.all()})

def add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient_id = form.cleaned_data['patient_id']
            new_name = form.cleaned_data['name']
            new_initials = form.cleaned_data['initials']
            new_sex = form.cleaned_data['sex']
            new_address = form.cleaned_data['address']
            new_post_card = form.cleaned_data['post_card']
            new_admission = form.cleaned_data['admission']
            new_DOB = form.cleaned_data['DOB']
            new_ward_id = form.cleaned_data['ward_id']
            new_next_of_kin = form.cleaned_data['next_of_kin']
            
            new_patient = P(
                patient_id=new_patient_id,
                name=new_name,
                initials=new_initials,
                sex = new_sex,
                address= new_address,
                post_card=new_post_card,
                admission=new_admission,
                DOB=new_DOB,
                ward_id=new_ward_id,
                next_of_kin=new_next_of_kin
            )
            new_patient.save()
            return render(request,'add.html',{
                'form':PatientForm(),
                'success': True
            })
    else:
        form = PatientForm()
    return render(request,'add.html',{'form': PatientForm()})
    
def edit(request,id):
    if request.method== 'POST':
        patient = P.objects.get(pk=id)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html',{
                'form':form,
                'success': True
            })
    else:
        patient = P.objects.get(pk=id)
        form = PatientForm(instance=patient)
    return render(request,'edit.html',{
        'form':form
        })

def delete(request,id):
    if request.method == 'POST':
        patient = P.objects.get(pk=id)
        patient.delete()
    return HttpResponseRedirect(reverse('index'))
