
from django.shortcuts import render, HttpResponse, redirect

layout="""
        <h1>Sitio Web con Django | Maria Buenaventura</h1>
        </hr>
        <ul>
            <li>
                <a href="/holaMundo">Hola Mundo</a>
            </li>
            <li>
                <a href="/saludo">Saludo</a>
            </li>

            <li>
                <a href="/index">Index</a>
            </li>

            
            <li>
                <a href="/contacto">Contacto</a>
            </li>

        </ul>
        """


def holaMundo (request):
    return HttpResponse(layout+"Hola Mundo desde Django")

def saludo(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto', name="a", lastName="aa")

    return HttpResponse(layout + """
                        <h1>Saludo de Bienvenida<h1/>
                        <h2>Bienvenidos al SENA Tolima<h2/>
                        """)

def contacto(request, name='', lastName=''):
    aprendiz = ""

    if name and lastName:
        aprendiz += f"""<h2>Nombre Completo: </h2>
                        <h3>{name} {lastName}</h3>
        """

    elif name:
        aprendiz += f"""<h2>Nombre: </h2>
                        <h3>{name} </h3>
        """

    elif name == '' and lastName:
        aprendiz += f"""<h2>Apellido: </h2>
                        <h3>{lastName}</h3>
        """    

    else:
        aprendiz += 'Sin información'

    return HttpResponse(layout + f"<h2>Contacto: </h2>" + aprendiz)


def index (request):
    template = """
                    <h1>Inicio</h1>
                    <p>Años desde el 2024 hasta el 2050</p>
                    <ul>
                        """

    year=2024
    while year <= 2050:
        template += f"<li> {str(year)} "
        if year % 2 == 0:
            template += "(Año par)"

        if  year % 4 == 0:
            template += "(Año bisiesto)"

        template+="</li>"
        year += 1

    template += "</ul>"

    return HttpResponse(layout+template)

