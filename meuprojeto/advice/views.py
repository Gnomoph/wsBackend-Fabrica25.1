import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Advice
from .forms import AdviceForm

def advice_list(request):
    advices = Advice.objects.all().order_by('-created_at')
    return render(request, 'advice_list.html', {'advices': advices})

def advice_detail(request, pk):
    advice = get_object_or_404(Advice, pk=pk)
    return render(request, 'advice_detail.html', {'advice': advice})

def advice_create(request):
    if request.method == 'POST':
        form = AdviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advice_list')
    else:
        # Se houver o parâmetro "fetch", buscamos a partir da API
        if request.GET.get('fetch') == 'true':
            url = "https://api.adviceslip.com/advice"
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                advice_text = data.get('slip', {}).get('advice', '')
                form = AdviceForm(initial={'text': advice_text})
            except requests.RequestException:
                form = AdviceForm()
        else:
            form = AdviceForm()
    return render(request, 'advice_form.html', {'form': form, 'action': 'Criar'})

def advice_update(request, pk):
    advice = get_object_or_404(Advice, pk=pk)
    if request.method == 'POST':
        form = AdviceForm(request.POST, instance=advice)
        if form.is_valid():
            form.save()
            return redirect('advice_list')
    else:
        form = AdviceForm(instance=advice)
    return render(request, 'advice_form.html', {'form': form, 'action': 'Atualizar'})

def advice_delete(request, pk):
    advice = get_object_or_404(Advice, pk=pk)
    if request.method == 'POST':
        advice.delete()
        return redirect('advice_list')
    return render(request, 'advice_confirm_delete.html', {'advice': advice})
