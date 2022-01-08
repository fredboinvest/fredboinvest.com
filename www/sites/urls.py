from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='index'),
	path('artikler/', artikler, name='artikler'),
	path('artikel/<slug:slug>', artikel, name='artikel'),
	path('kontakt', kontakt, name='kontakt'),
	path('who-am-i', who_am_i, name="who-am-i"),
	path('trading', trading, name="trading"),

	#Json Requests
	path('investment_quotes', investment_quotes, name="investment_quotes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)