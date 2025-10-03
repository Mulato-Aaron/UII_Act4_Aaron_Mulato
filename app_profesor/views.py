from django.shortcuts import render

def index(request):
    """
    Muestra una lista de profesores en una página web.
    """
    profesores = [
        {
            'nombre': 'Aaron Mulato',
            'materia': 'Programación Avanzada',
            'email': 'aaron.mulato@empresa.com'
        },
        {
            'nombre': 'Ing. Juan Pérez',
            'materia': 'Bases de Datos',
            'email': 'juan.perez@empresa.com'
        },
        {
            'nombre': 'Lic. María López',
            'materia': 'Desarrollo Web',
            'email': 'maria.lopez@empresa.com'
        },
    ]
    contexto = {'profesores': profesores}
    return render(request, 'index.html', contexto)