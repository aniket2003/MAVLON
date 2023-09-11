# views.py

from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from django.conf import settings

def login_with_salesforce(request):
    # return render(request, 'salesforce_login.html')
    print("logging in with salesforce")
    salesforce_auth_url = f'https://login.salesforce.com/services/oauth2/authorize?' \
                          f'response_type=code&' \
                          f'client_id={settings.SALESFORCE_CLIENT_ID}&' \
                          f'redirect_uri={settings.SALESFORCE_REDIRECT_URI}&' \
                          f'state=your_custom_state'
    return redirect(salesforce_auth_url)

def salesforce_callback(request):
    print("got a callback")
    code = request.GET.get('code')
    if code:
        token_url = 'https://login.salesforce.com/services/oauth2/token'
        token_data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': settings.SALESFORCE_CLIENT_ID,
            'client_secret': settings.SALESFORCE_CLIENT_SECRET,
            'redirect_uri': settings.SALESFORCE_REDIRECT_URI,
        }
        response = requests.post(token_url, data=token_data)
        if response.status_code == 200:
            json_response = response.json()
            access_token = json_response['access_token']
            return render(request, 'welcome.html')
    return HttpResponse('Salesforce OAuth failed.')



def homepage(request):
    return render(request, 'salesforce_login.html')
    # return redirect(salesforce_auth_url)


def logout(request):
    request.session.flush()
    return redirect('homepage')