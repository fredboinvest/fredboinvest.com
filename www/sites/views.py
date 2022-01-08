from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core import serializers

# Create your views here.
def index(request):

	recent_articles = ArticleModel.objects.filter(is_published=True).order_by('-article_date')[:5]

	data = {
		'articles': recent_articles
	}
	return render(request, 'index.html', data)

article_search = ""
def artikler(request):
	all_articles = ArticleModel.objects.filter(is_published=True)
	global article_search
	try:
		page_number = int(request.GET.get('page'))
	except:
		article_search = ""
		page_number = 1

	if request.GET.get('article-search') != None:
		article_search = request.GET.get('article-search')
		header_articles = all_articles.filter(article_header__icontains=request.GET.get('article-search'))
		tag_articles = all_articles.filter(tag__tag__icontains=request.GET.get('article-search'))

		filtered_articles = ArticleModel.objects.none()
		filtered_articles = filtered_articles.union(header_articles, tag_articles).order_by('-article_date')
	else:
		filtered_articles = all_articles.order_by('-article_date')

	articles_paginator = Paginator(filtered_articles, 3)
	if page_number > articles_paginator.num_pages:
		page_number = articles_paginator.num_pages
	elif page_number < 1:
		page_number = 1
	current_articles = articles_paginator.page(page_number)
	data = {
		'current_page': current_articles,
		'paginator': articles_paginator,
		'article_search': article_search,
		'tags': TagModel.objects.all()
	}

	return render(request, 'artikler.html', data)


def artikel(request, slug):
	data = {
		'article': ArticleModel.objects.get(article_slug=slug)
	}

	return render(request, 'artikel.html', data)

def kontakt(request):

	return render(request, 'kontakt.html')

def who_am_i(request):

	return render(request, 'who_am_i.html')

date_from = ""
date_to = ""
def trading(request):
	all_trading_days = TradingDay.objects.all().order_by('trading_date')
	global date_from
	global date_to

	try:
		page_number = int(request.GET.get('page'))
	except:
		date_from = ""
		date_to = ""
		page_number = 1

	if request.GET.get('date-from') != "" and request.GET.get('date-from') != None and request.GET.get('date-to') != "" and request.GET.get('date-to') != None:
		date_from = request.GET.get('date-from')
		date_to = request.GET.get('date-to')

		filtered_trading_days = all_trading_days.filter(trading_date__gte=date_from, trading_date__lte=date_to)


		if str(date_from) == str(all_trading_days.first().trading_date):
			previous_trading_day = all_trading_days.filter(trading_date__lte=date_from).first()
		else:
			previous_trading_day = all_trading_days.filter(trading_date__lt=date_from).last()
	else:
		filtered_trading_days = all_trading_days
		previous_trading_day = all_trading_days.first()

	filtered_trading_days = filtered_trading_days.order_by('trading_date')

	trading_days_paginator = Paginator(filtered_trading_days.order_by('-trading_date'), 10)
	if page_number > trading_days_paginator.num_pages:
		page_number = trading_days_paginator.num_pages
	elif page_number < 1:
		page_number = 1

	current_trading_days = trading_days_paginator.page(page_number)

	data = {
		'filtered_trading_days': filtered_trading_days,
		'previous_trading_day': previous_trading_day,
		'current_page_trading_days': current_trading_days,
		'paginator': trading_days_paginator,
		'date_from': date_from,
		'date_to': date_to,
		'first_trading_day': all_trading_days.first(),
		'last_trading_day': all_trading_days.last()
	}

	return render(request, 'trading.html', data)

def investment_quotes(request):
	data = {
		'data': list(InvestmentQuoteModel.objects.all().values())
	}

	return JsonResponse(data)




















