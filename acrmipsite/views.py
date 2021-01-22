from django.shortcuts import render

from django.shortcuts import render


def home(request):
    return render(request, 'acrmipsite/home.html')


def about(request):
    return render(request, 'acrmipsite/about_us.html')


def research(request):
    return render(request, 'acrmipsite/research.html')


def team(request):
    return render(request, 'acrmipsite/our_team.html')


def partnership(request):
    return render(request, 'acrmipsite/partnership.html')


def csi_jump(request):
    return render(request, 'acrmipsite/csi_jump.html')


def lln_es(request):
    return render(request, 'acrmipsite/lifelinesnets_es.html')


def lln_tr(request):
    return render(request, 'acrmipsite/lifelinesnets_tr.html')


def smart_grid(request):
    return render(request, 'acrmipsite/smart_grid.html')


def iec_stds_conformity(request):
    return render(request, 'acrmipsite/iec_stds_conform.html')


def acfta_iec_stds_eco(request):
    return render(request, 'acrmipsite/acfta_iec_stds_eco.html')


def illie_dp(request):
    return render(request, 'acrmipsite/illie_dis_protect.html')
