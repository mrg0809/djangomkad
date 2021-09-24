from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
# Create your views here.

def calculateDistanceView(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)

    context = {
        'distance' : obj,
        'form' : form,
    }

    return render(request, 'measurements/index.html', context)