from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse

def get_api_pessoas(request):
    response = requests.get('http://localhost:5000/pessoas')
    pessoas = response.json()
    return pessoas

def listar_pessoas(request):
    pessoas = get_api_pessoas(request)
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})

def home(request):
    return render(request, 'home.html')

def atualizar_pessoas(request, pessoa_id):
    response = requests.get(f'http://localhost:5000/pessoas/{pessoa_id}')

    if response.status_code == 200:
        pessoa = response.json()

        if request.method == 'POST':
            nome = request.POST['nome']
            rg = request.POST['rg']
            cpf = request.POST['cpf']
            data_nascimento = request.POST['data_nascimento']
            data_admissao = request.POST['data_admissao']
            funcao = request.POST['funcao']
            data_atualizacao = {
                'nome': nome,
                'rg': rg,
                'cpf': cpf,
                'data_nascimento': data_nascimento,
                'data_admissao': data_admissao,
                'funcao': funcao,
            }

            response = requests.put(f'http://localhost:5000/pessoas/{pessoa_id}', json=data_atualizacao)
            
            if response.status_code == 200:
                return redirect('listar_pessoas')
            else:
                return HttpResponse('Falha na atualização', status=500)

        return render(request, 'atualizar_pessoas.html', {'pessoa': pessoa})
    else:
        return HttpResponse('Pessoa não encontrada', status=404)



def deletar_pessoas(request, pessoa_id):
    if request.method == 'GET':
        requests.delete(f'http://localhost:5000/pessoas/{pessoa_id}')

    return redirect('listar_pessoas')


def adicionar_pessoas(request):
    if request.method == 'POST':
        data = {
            'nome': request.POST['nome'],
            'rg': request.POST['rg'],
            'cpf': request.POST['cpf'],
            'data_nascimento': request.POST['data_nascimento'],
            'data_admissao': request.POST['data_admissao'],
            'funcao': request.POST['funcao'],
        }
        response = requests.post('http://localhost:5000/pessoas', json=data)
        if response.status_code == 201:
            return redirect('listar_pessoas')
        else:
            return HttpResponse('Erro ao adicionar pessoa', status=400)

    return redirect('listar_pessoas')

def editar_pessoas(request):
    pessoas = get_api_pessoas(request)
    return render(request, 'editar_pessoas.html', {'pessoas': pessoas})
