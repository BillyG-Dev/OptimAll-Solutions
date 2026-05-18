from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DeploymentBriefForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = DeploymentBriefForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                "System Brief Securely Transmitted. Our engineering unit will contact you within 24 hours."
            )
            return redirect('contact')
        else:
            messages.error(request, "Transmission failed. Please check your data parameters.")
    else:
        form = DeploymentBriefForm()
        
    return render(request, 'contact.html', {'form': form})

