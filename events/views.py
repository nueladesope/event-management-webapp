from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

# Create your views here.
def event_list(request):    # defines a view function that takes a request parameter
    events = Event.objects.all()    # Event.objects.all() retrieves all Event objects from the database
    return render(request, 'event_list.html', {'events': events})    # returns a rendered template with all events passed as context data

def event_detail(request, pk):    # takes request and primary key (pk) as parameters
    event = get_object_or_404(Event, pk=pk)   # finds the event with the given primary key or shows 404 error
    return render(request, 'event_detail.html', {'event': event})     # renders the event detail template with the specific event
    
def add_event(request):    # defines a view function that takes a request parameter
    if request.method == 'POST':    # checks if the request method is POST
        form = EventForm(request.POST)    # creates a form instance with the submitted data
        if form.is_valid():   # checks if the form is valid
            form.save()    # saves the form data to the database
            return redirect('event_list')    # redirects to the event list view
    else:    # if the request method is not POST
        form = EventForm()    # creates a new empty form instance
    return render(request, 'event_form.html', {'form': form, 'title': 'Add Event'})    # renders the event form template with the form and title

def update_event(request, pk):    # takes request and primary key (pk) as parameters
    event = Event.objects.get(pk=pk)    # finds the event with the given primary key or shows 404 error
    if request.method == 'POST':    # checks if the request method is POST
        form = EventForm(request.POST, instance=event)    # creates a form instance with the submitted data and the event instance
        if form.is_valid():    # checks if the form is valid
            form.save()    # saves the form data to the database
            return redirect('event_list')    # redirects to the event list view
    else:    # if the request method is not POST
        form = EventForm(instance=event)    # creates a form instance prepopulated with the existing event data
    return render(request, 'event_form.html', {'form': form, 'title': 'Update Event'})    # renders the event form template with the form and title

def delete_event(request, pk):    # takes request and primary key (pk) as parameters
    event = Event.objects.get(pk=pk)    # finds the event to be deleted with the given primary key
    if request.method == 'POST':    # checks if the request method is POST
        event.delete()    # deletes the event
        return redirect('event_list')    # redirects to the event list view
    return render(request, 'event_confirm_delete.html', {'event': event})    # renders the event confirm delete template with the event
    
