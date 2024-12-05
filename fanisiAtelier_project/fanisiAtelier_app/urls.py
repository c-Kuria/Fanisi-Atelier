from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('top-5-interior-design-trends-2024/', views.top_5_interior_design_trends_2024, name='top-5-interior-design-trends-2024'),
    path('how-to-choose-the-right-color-palette-for-your-home/', views.how_to_choose_the_right_color_palette_for_your_home, name='how-to-choose-the-right-color-palette-for-your-home'),
    path('maximazing-small-spaces-design-tips-and-tricks/', views.maximazing_small_spaces_design_tips_and_tricks, name='maximazing-small-spaces-design-tips-and-tricks'),
    path('the-importance-of-lighting/', views.the_importance_of_lighting, name='the-importance-of-lighting'),
    path('send_email/', views.send_email, name='send_email'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]