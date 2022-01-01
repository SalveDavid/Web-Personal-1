from django.shortcuts import render, HttpResponse


# def home(request):
#     html_response = '<h1>Mi web personal</h1>'
#     for i in range(10):
#         html_response += '<h2>Portada---</h2>'
#     return HttpResponse(html_response)

html_base = '''
<h1>Mi web personal</h1>
<ul>
    <li><a href='/'>Portada</a></li>
    <li><a href='/about-me'>Acerca de</a></li>
    <li><a href='/portfolio'>Portafolio</a></li>
    <li><a href='/contact'>Contacto</a></li>
</ul>
'''


def home(request):

    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')
    # return HttpResponse(html_base + '<h1>Mi web personal</h1><h2>Acerca de</h2>'
    #                                 '<p>Me llamo David y soy programador</p>')



    # return HttpResponse(html_base + '<h1>Mi web personal</h1><h2>Este es mi portafolio</h2>'
    #                                 '<p>CSS, HTML, PYTHON, SQL</p>')


def contact(request):
    return render(request, 'core/contact.html')
    # return HttpResponse(html_base + '<h1>Mi web personal</h1><h2>Para contactarme</h2>'
    #                                 '''<ol>
    #                                         <li>Telefono</li>
    #                                         <li>Correo</li>
    #                                         <li>Twitter</li>
    #                                         <li>Instagram</li>
    #                                     </ol>''')
