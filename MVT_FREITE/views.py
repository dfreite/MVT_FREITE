from django.http import HttpResponse
from django.template import Template, Context
from datetime import date


def family(self):

    mom = ["Victoria", int(50), date(1970,1,1)]
    dad = ["Victor", int(50), date(1970,2,2)]
    bro = ["Vict", int(10), date(2012,3,3)]

    family_dict = {
        "MomName": mom[0], "MomAge": mom[1], "MomNac": mom[2],
        "DadName": dad[0], "DadAge": dad[1], "DadNac": dad[2],
        "BroName": bro[0], "BroAge": bro[1], "BroNac": bro[2]
    }
    miHtml = open("C:/Users/Marengo/MVT_FREITE/MVT_FREITE/template/template1.html")
    plantilla = Template(miHtml.read())    
    miHtml.close()
    miContexto = Context(family_dict) 
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)