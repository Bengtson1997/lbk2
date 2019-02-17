from django.contrib import admin
from django.urls import path

#from pages.views import login_view
from django.contrib.auth.views import LoginView, LogoutView
from projekt.views import (
							projekt_detail_view, 
							projekt_create_view, 
							projekt_delete_view, 
							projekt_list_view, 
							profil_view, 
							projekt_update_view, 
							#login_view
							)
	
app_name = 'projekt'
urlpatterns = [
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('', projekt_list_view, name='projekter'),
	path('profil/', profil_view, name='profil'), 
	path('create/', projekt_create_view, name='projekt_oprettelse'),
	path('<int:my_id>/', projekt_detail_view, name='projekt_detaljer'),
	path('<int:my_id>/update/', projekt_update_view, name='opdater_projekt'),
	path('<int:my_id>/delete/', projekt_delete_view, name='slet_projekt'),

]