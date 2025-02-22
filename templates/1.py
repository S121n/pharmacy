from django.shortcuts import render
from django.http import JsonResponse
from dr.models import Patient
from Viper.models import Medicine, PatientMedicine

def order_page(request):
    if request.method == "POST":
        national_id = request.POST.get("national_id")

        if not national_id:
            return JsonResponse({"message": "National ID is required!"}, status=400)

        try:
            patient = Patient.objects.get(national_id=national_id)
        except Patient.DoesNotExist:
            return JsonResponse({"message": "Patient not found!"}, status=404)

        prescribed_medicines = PatientMedicine.objects.filter(patient=patient).select_related('medicine')

        available_drugs = []
        for prescription in prescribed_medicines:
            medicine = Medicine.objects.filter(generic_code=prescription.medicine.generic_code, available=True).first()
            if medicine:
                available_drugs.append({
                    "name": medicine.name,
                    "generic_code": medicine.generic_code,
                    "effective_dose": medicine.effective_dose,
                    "pharmaceutical_form": medicine.pharmaceutical_form,
                    "description": medicine.description,
                    "image": medicine.get_url(),
                })

        if not available_drugs:
            return JsonResponse({"message": "No matching drugs found in the pharmacy!"}, status=404)

        return JsonResponse({"drugs": available_drugs})

    return render(request, "order.html")
