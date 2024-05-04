from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        api_url = f'http://127.0.0.1:8000/stocks/{name}' 
        response = requests.get(api_url)
        if response.status_code == 200:
            company_data = response.json()
            return render(request, 'results.html', {'company_data': company_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch company results. Check Again!'})
    
        
    return render(request, 'index.html')