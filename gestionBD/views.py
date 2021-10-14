import json
from django.http.response import JsonResponse
from django.shortcuts import render
from gestor.utils.article import create_article

def admin_root(request):
  return render(request, 'admin/index.html')

def add_vehicle(request):
  body = bytes_to_dict(request.body)
  print(body)
  create_article(body)
  return JsonResponse({
    'ok': True,
  })

def bytes_to_dict(bytes)->dict:
  return json.loads(bytes.decode('utf-8'))