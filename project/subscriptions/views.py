from django.http.response import HttpResponse
from django.shortcuts import render
from project.subscriptions.forms import SubscriptionForm
from django.http import HttpResponseRedirect
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)

            mail.send_mail('Confirmação de inscrição', body,
                           'mrpsousa@outlook.com',
                           ['mrpsousa@outlook.com', form.cleaned_data['email']])
            
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
