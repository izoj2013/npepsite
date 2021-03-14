from django.shortcuts import render

from django.shortcuts import render

homeTitles = ["Welcome to the African Computing Renaissance Home Page!",
             "About Us Page!",
             "ACFTA IEC Standards Ecosystem!",
             "Computer Science Impossibility Jump!",
             "IEC Standards Conformity!",
             "Integrated Lifelines Infrastructure Emergency - Disaster Protection!",
             "LifeLinesNets Emergency States Page!",
             "LifeLinesNets Topological Reliability Page!",
             "Partner With Us",
             "Our Research Areas Page!",
             "Smart Grid Systems @EEE Research Group - UNZA"
            ]
homeTitle = "Welcome to the African Computing Renaissance Home Page!"
imgURL = "acrmipsite/images/home_computer_board.jpg"
loremHeader = "lorem 3 p"
loremContentTxt = 'lorem 10 b random'


def home(request):
    return render(request, 'acrmipsite/home.html',
                  context= {
                      'title': homeTitle,
                      'imgUrl': imgURL,
                      'hdrText': loremHeader,
                      'contentTxt': loremContentTxt
                  })


def about(request):
    return render(request, 'acrmipsite/about_us.html')


def research(request):
    return render(request, 'acrmipsite/research.html')


def team(request):
    return render(request, 'acrmipsite/our_team_a.html')


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
