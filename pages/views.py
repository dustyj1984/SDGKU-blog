from django.views.generic import TemplateView
from bs4 import BeautifulSoup
import requests

URL = "https://wttr.in/San+Diego"
HEADER = {
    "User-Agent": (
        'Mozilla/5.0 (Macintosh; Intel Mac' 
        'OS X 10_15_7) AppleWebKit/537.36 (K'
        'HTML, like Gecko) Chrome/107.0.0.0' 
        'Safari/537.3'
    )

}


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class WeatherPageView(TemplateView):
    template_name = 'pages/weather.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        response = request.get(URL, headers=HEADER)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_pre = soup.find("pre")
        else:
            weather_pre = "%s" % response.text
        context['weather'] = str(weather_pre)
        return self.render_to_response(context)
    
