from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acr-home'),
    path('about/', views.about, name='about-us'),
    path('research/', views.research, name='research'),
    path('team/', views.team, name='team'),
    path('partnership/', views.partnership, name='partnership'),
    path('csi-jump/', views.csi_jump, name='csi-jump'),
    path('lifelinesnets-es/', views.lln_es, name='lln-es'),
    path('lifelinesnets-tr/', views.lln_tr, name='lln-tr'),
    path('smart-grid/', views.smart_grid, name='smart-grid'),
    path('iec-standards-conformity/',
         views.iec_stds_conformity, name='iec-stds-conform'),
    path('acfta-iec-standards-ecosystem',
         views.acfta_iec_stds_eco, name='acfta-iec-stds-eco'),
    path('integrated-lifelines', views.illie_dp, name='illie-dp'),
]
