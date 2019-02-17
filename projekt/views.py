from django.shortcuts import render, get_object_or_404, redirect

from .forms import RawProjektForm, ProjektForm

from .models import projekt 

from django.contrib.auth.decorators import login_required

# Create your views here.

#def login_view(request):

#	return render(request, "login.html", {}) 

@login_required
def profil_view(request):

	return render(request, "profil.html", {}) 

@login_required
def projekt_create_view(request):
	form = ProjektForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('../')
	context = {
		"form": form		
		}
	return render(request, "projektdetailsfolder/projektcreate.html", context)

@login_required
def projekt_update_view(request, my_id=id):
	obj = get_object_or_404(projekt, id=my_id)
	form = ProjektForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('../')
	context = {
		'form': form
		}
	return render(request, "projektdetailsfolder/projektcreate.html", context)

@login_required
def projekt_delete_view(request, my_id):
	obj = get_object_or_404(projekt, id=my_id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"object_delete": obj	
		}
	return render(request, "projektdetailsfolder/projektdelete.html", context)

@login_required
def projekt_detail_view(request, my_id):
	obj = get_object_or_404(projekt, id=my_id)
	context = {
		"object_detail": obj			
		}
	return render(request, "projektdetailsfolder/projektdetail.html", context)

@login_required
def projekt_list_view(request, *args, **kwargs):
	queryset = projekt.objects.all()
	context = {
		"object_list": queryset 
	}
	return render(request, "projekt.html", context)