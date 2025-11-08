from django.urls import path 
from pages import views

urlpatterns = [
    path('', views.paginas_view, name='home'),
    path('sobre/', views.paginas_view, name='sobre'), 
    path('faq/', views.paginas_view, name='faq'), 
    path('contato/', views.paginas_view, name='contato'),
    
    path('omnilife/', views.omnilife_view, name='omnilife'),
    path('eletrofitness/', views.eletrofitness_view, name='eletrofitness'),
    path('procedimentos/', views.procedimentos_view, name='procedimentos'),
    path('jalecos/', views.jalecos_view, name='jalecos'),
    path('melasma/', views.melasma_view, name='melasma'),
]
