from django.views.generic.base import TemplateView
from .models import Gig
from datetime import datetime, timedelta

# Create your views here.
class HomeView(TemplateView):
    template_name = "home/index.html"

class MenuView(TemplateView):
    template_name = "home/menu.html"

class PhotoView(TemplateView):
    template_name = "home/photos.html"

class EventView(TemplateView):
    template_name = "home/events.html"

    def get_context_data(self, **kwargs):
        now = datetime.now()
        all_gigs = Gig.objects.order_by('date')
        # Get future gigs
        future_gigs = [gig for gig in all_gigs if gig.date >= now.date()]
        # Get gigs within 7 days of today
        this_week = [gig for gig in future_gigs if gig.date - timedelta(days=7) <= now.date()]
        context = super().get_context_data(**kwargs)
        context['all_egigs'] = all_gigs
        context['future_gigs'] = future_gigs
        context['this_week'] = this_week
        return context