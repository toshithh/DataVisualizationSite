from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Data


def index(request):
    def distinct(x):
        nx = []
        for e in x:
            if e[0] not in nx:
                nx.append(e[0])
        return nx
    template = loader.get_template("index.html")
    data = Data.objects
    topics = distinct(data.order_by('topic').values_list('topic'))
    endyear =  distinct(data.order_by('end_year').values_list('end_year'))
    sector =  distinct(data.order_by('sector').values_list('sector'))
    region =  distinct(data.order_by('region').values_list('region'))
    source =  distinct(data.order_by('source').values_list('source'))
    country =  distinct(data.order_by('country').values_list('country'))

    context = {
        'topics': topics,
        'endyear': endyear,
        'sector': sector,
        'region': region,
        'source': source,
        'country': country,
    }
    return HttpResponse(template.render(context, request))

def fetch(request):
    if request.GET:
        topic1 = request.GET["topic"]
        endyear1 = request.GET['endyear']
        sector1 = request.GET['sector']
        region1 = request.GET['region']
        source1 = request.GET['source']
        country1 = request.GET['country']
        data = Data.objects.all().order_by("start_year")
        if topic1:
            data = data.filter(topic=topic1)
        if endyear1:
            data = data.filter(end_year=endyear1)
        if sector1:
            data = data.filter(sector=sector1)
        if region1:
            data = data.filter(region=region1)
        if source1:
            data = data.filter(source=source1)
        if country1:
            data = data.filter(country=country1)
        data = str(list(data.values("intensity", "likelihood","relevance","start_year","country","topic","region","end_year")))
        data = data.replace("'", "\"")
        data = data.replace("None", "\"\"")
        
        return HttpResponse(data, content_type="text/plain")

