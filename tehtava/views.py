from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.

def home(request):
    

    return render(request, 'accounts/home.html')

def antiqua(request):
    antiqua_json = read_antiqua_json()

    return render(request, 'accounts/antiqua.html', {'antiqua_json':antiqua_json})


def read_antiqua_json():
    # #Avaa tiedosto ja lue tiedosto
    # f = open("E:\\Solita Tehtävä\solita_tehtava\json_files\Antiqua.source", "r")    
    # r = f.read()
    # f.close()
    # #antique_json = r
    # antique_json = json.load(r)

    # print("\n\nTESTII = ", antique_json)

    # return antique_json

    #Toimii oikein, saa sekä list ja dict
    table = []
    with open('E:\\Solita Tehtävä\solita_tehtava\json_files\Antiqua.source', 'r') as f:
        for line in f:
            try:
                j = line.split('|')[-1]
                table.append(json.loads(j))
            except ValueError:
                # You probably have bad JSON
                continue

    # for row in table:
    #     print("\n\n\n JOU JOU =", type (row)) # type dict

    #print("\n\n TYYPPPI table = ", table) # type list
    return table
    

def solar(request):
    solar_json = read_solar_json()   
    solar_json = time_change(solar_json)

    return render(request, 'accounts/solar.html', {'solar_json':solar_json})

def read_solar_json():
    #Toimii oikein, saa sekä list ja dict
    table = []
    with open('E:\\Solita Tehtävä\solita_tehtava\json_files\SolarBuddhica.source', 'r') as f:
        for line in f:
            try:
                j = line.split('|')[-1]
                table.append(json.loads(j))
            except ValueError:
                # You probably have bad JSON
                continue

    return table

def time_change(json):

    muutettu = 0
    for parse in json:
        x = parse.items()
        time_value = parse['arrived']
        time = time_value.split("T")
        muutettu = time[0]
        parse["arrived"] = muutettu

    return json






