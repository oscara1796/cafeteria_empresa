from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from contact.forms import ContactForm

# Create your views here.


def contact(request):
    # print(f' Tipo de petición {request.method}')
    contact_form = ContactForm()

    if request.method== "POST":
        contact_form = ContactForm(data= request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            #Enviamos el correo y redireccionamos
            email= EmailMessage(
                f"La caffetiera nuevo mensaje de contacto {name}",
                f"De {name} <{email}> \n\nEscibió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["oscara1706cl@gmail.com", "083a4d0ef4-cabaf3@inbox.mailtrap.io"],
                reply_to=[email]

            )
            try:
                email.send()
                return redirect(reverse('contacto')+'?ok')
            except:
                return redirect(reverse('contacto')+'?fail')



    return render(request, "contact/contact.html",{'form': contact_form})
