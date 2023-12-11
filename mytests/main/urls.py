from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('tester/<int:id>/<int:id_task>/<int:pk>', views.tester, name='tester'),
	path('tester/<int:id>', views.tester, name='tester'),
	path('tester', views.tester, name='tester'),
	path('result/<int:pk>', views.result, name='result'),
	path('results/', views.ResultListView.as_view(), name='results'),
]