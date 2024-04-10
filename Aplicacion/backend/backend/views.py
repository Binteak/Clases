from django.http import JsonResponse

def mi_vista(request):
    # Aquí obtienes tus datos, por ejemplo, desde tu modelo Django
    data = [{'id': 1, 'name': 'Ejemplo 1'}, {'id': 2, 'name': 'Ejemplo 2'}]
    print(data)
    return JsonResponse(data, safe=False)