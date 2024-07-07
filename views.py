from django.http import JsonResponse
from BTS.models import Routes
from django.shortcuts import render, HttpResponse,get_object_or_404

from django.utils import timezone
from .forms import SearchForm

def index(request):
    form = SearchForm()
    route_data = None
    current_time = timezone.localtime().time()  # Get the current local time

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['source']
            destination = form.cleaned_data['destination']
            # Query MongoDB for the route with the current time as departure time
            route_data= Routes.objects.filter(
                Source=source,
                Destination=destination,
                #departure_time=current_time,
            ).first()

    return render(request, 'index.html', {'form': form, 'route_data': route_data})




#from .forms import RouteSearchForm
def home(request):
    return render(request,"home.html")
def search(request):
    return render(request,"search.html")
# Create your views here.
#def home(request):
#    if request.method == 'GET':
 #       source = request.GET.get('Source')
 ###       destination = request.GET.get('Destination')

       # if Source and Destination:
           # context = {
                
                #'number':Routes.objects.all()filter()
               # 'Source' :
               # 'Destination' :
              ##  'Src ': 
                #'Dest' : 
               # 'Stops' :
            #}
   # return render(request,"home.html", context)
#from .models import Bus, Location


def map(request):
    return render(request, 'map.html')

def about(request):
    return render(request, 'btabout.html')

# views.py
  # Import your Routes model

#from django.shortcuts import get_object_or_404
#from django.views.decorators.csrf import csrf_exempt

#def get_bus_status(request, bus_number):
#    route = get_object_or_404(Routes, number=bus_number)
#    current_time = localtime().time()
#    departure_time = route.departure_time

#    if route.status == 'notStarted' and current_time >= departure_time:
#        route.status = 'started'
#        route.save()

#    return JsonResponse({
#        'status': route.status,
#        'bus_position': route.get_Src(),  # Assuming Src is used for current position
#        'departure_time': str(departure_time),
#        'current_time': str(current_time)
#    })

#@csrf_exempt
#def update_bus_status(request, bus_number):
#    if request.method == 'POST':
#        route = get_object_or_404(Routes, number=bus_number)
#        status = request.POST.get('status')
#        if status:
#            route.status = status
#            route.save()
#        return JsonResponse({'status': 'success'})

#@csrf_exempt
#def reset_bus_tracking(request, bus_number):
#    if request.method == 'POST':
#        route = get_object_or_404(Routes, number=bus_number)
#        route.status = 'notStarted'
#        route.Src = '[]'
#        route.save()
#        return JsonResponse({'status': 'success'})


from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_route(request):
    route = Routes.objects.first()  # Assuming a single route for simplicity
    return JsonResponse({
        'source': route.Src,
        'destination': route.Dest,
        'departure_time': route.departure_time.strftime('%H:%M:%S'),
        'destination_name': route.Destination
    })

@csrf_exempt
def check_departure(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        current_time = data.get('current_time')
        route = Routes.objects.first()  # Assuming a single route for simplicity
        
        if route.departure_time.strftime('%H:%M:%S') == current_time:
            route.status = 'started'
            route.save()
            message = 'The bus has started.'
        elif route.departure_time.strftime('%H:%M:%S') > current_time:
            message = 'The bus has not started yet.'
        else:
            message = 'The bus has already departed.'

        return JsonResponse({'message': message, 'status': route.status})

@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')
        route = Routes.objects.first()
        route.status = status
        route.save()
        return JsonResponse({'message': f'Status has been updated to {status}.'})

@csrf_exempt
def reset_status(request):
    if request.method == 'POST':
        route = Routes.objects.first()
        route.status = 'notStarted'
        route.save()
        return JsonResponse({'message': 'Status has been reset.', 'status': route.status})

@csrf_exempt
def swap_source_destination(request):
    if request.method == 'POST':
        route = Routes.objects.first()
        route.Source, route.Destination = route.Destination, route.Source
        route.Src, route.Dest = route.Dest, route.Src
        route.status = 'started'
        route.save()
        return JsonResponse({
            'message': 'Source and destination have been swapped.',
            'status': route.status
        })

