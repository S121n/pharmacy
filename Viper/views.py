from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request

from Viper.forms import UploadForm
from Viper.models import Medicine, ContactUs, PatientMedicine
from dr.models import Patient,Drug


# Create your views here.
def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'home.html', {'medicines': medicines})

def order(request):
    return render(request, 'order.html')


# Upload Def
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})

# ContactUs
def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')

        ContactUs.objects.create(name=user_name, email=user_email, message=user_message)
        return redirect('home')

# Search
def search(request):
    query = request.GET.get('query')
    medicines = Medicine.objects.all()
    if query:
        medicines = medicines.filter(
                                        Q(name__icontains=query)|
                                        Q(effective_dose__icontains=query)|
                                        Q(generic_name__icontains=query)|
                                        Q(generic_code__icontains=query)|
                                        Q(pharmaceutical_form__icontains=query)
        )
    return render(request, 'search.html', {'medicines': medicines})



#Order

def order_page(request):
    available_drugs = []
    unavailable_drugs = []
    error_message = None

    if request.method == "POST":
        national_id = request.POST.get("national_id")

        if not national_id:
            error_message = "National ID is required!"
        else:
            try:
                patient = Patient.objects.get(national_id=national_id)

                # دریافت داروهای تجویز شده از مدل Drug
                prescribed_drugs = Drug.objects.filter(patient=patient)

                for drug in prescribed_drugs:
                    medicine = Medicine.objects.filter(generic_code=drug.generic_code).first()

                    if medicine and medicine.available:
                        available_drugs.append(medicine)
                    else:
                        unavailable_drugs.append(drug)  # دارویی که در داروخانه موجود نیست

                if not available_drugs and not unavailable_drugs:
                    error_message = "No matching drugs found in the pharmacy!"

            except Patient.DoesNotExist:
                error_message = "Patient not found!"

    return render(request, "order.html", {
        "available_drugs": available_drugs,
        "unavailable_drugs": unavailable_drugs,
        "error_message": error_message
    })

# Detail
def medicine_detail(request,id):
    medicine = get_object_or_404(Medicine, id=id)
    return render(request, 'info.html', {'medicine': medicine})