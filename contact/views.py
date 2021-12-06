from django.shortcuts import render

# Create your views here.
from contact.forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'contact/thanks.html')
    context = {'form': form}
    return render(request, 'contact/contact.html', context)