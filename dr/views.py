from django.shortcuts import render
from django.http import JsonResponse
from .models import Patient, Drug

def drug_entry(request):
    if request.method == "POST":
        national_id = request.POST.get("national_id")
        name = request.POST.get("name")
        effective_dose = request.POST.get("effective_dose")
        generic_code = request.POST.get("generic_code")

        if not national_id or not name or not effective_dose or not generic_code:
            return JsonResponse({"message": "All fields are required!"}, status=400)

        try:
            patient, created = Patient.objects.get_or_create(national_id=national_id)
            Drug.objects.create(
                patient=patient,
                name=name,
                effective_dose=effective_dose,
                generic_code=generic_code
            )
            return JsonResponse({"message": "Drug added successfully!"})
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)

    return render(request, "drug_entry.html")
