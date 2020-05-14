from django.shortcuts import render, HttpResponse

html_base ="""
<h1>Mi Web Personal Sandra</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="about-me">Acerca de </a></li>
    <li><a href="contact">Contacto</a></li>
    <li><a href="portfolio">Portafolio </a></li>
   
</ul>

"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Hola mi nombre es Sandra Gutierrez, me gusta programar y estoy apfrendiendo Django</p>
    """)
def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí dejo mi email y mis redes sociales</p>
        <ul>
            <li><a href="sandra2202gutierrez@gmail.com">Email</a></li>
            <li><a href="https://youtube.com"></a>Facebook</li>
        </ul>

    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portafolio</h2>
        <p>Algunos de mis trabajos </p>
    """)