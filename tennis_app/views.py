from django.views.generic import ListView, DetailView, TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import TennisClub, Member, Competition
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ClubListView(ListView):
    model = TennisClub
    template_name = 'club_list.html'
    context_object_name = 'all_clubs_list'

class CompListView(ListView):
    model = Competition
    template_name = 'comp_list.html'
    context_object_name = 'all_comps_list'

class MemListView(ListView):
    model = Member
    template_name = 'mem_list.html'
    context_object_name = 'all_mems_list'


class CompDetailView(DetailView):
    model = Competition
    template_name = 'comp_detail.html'

class CompCreateView(CreateView):
    model = Competition
    template_name = 'comp_create.html'
    fields = ['name', 'date','tennis_club','participants']

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'club_name': None,
        'error_message': None,
    }

    try:
        oldest_club = TennisClub.objects.earliest('established_date')
        context['club_name'] = oldest_club.name

    except TennisClub.DoesNotExist:
        context['error_message'] = "No clubs found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)


def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'competitions': None,
        'error_message': None,
    }

    try:
        # Retrieve all dogs and sort them by name in ascending order
        competitions = Competition.objects.all()

        if not competitions:
            context['message'] = "No competitions found."
        else:    
            # Update the context with the list of competitions
            context['competitions'] = competitions

    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query2.html', context)


