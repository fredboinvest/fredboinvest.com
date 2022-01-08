from django import template
from ..models import ArticleModel, TagModel

register = template.Library()

@register.simple_tag
def get_related_articles(article):
	article_tag = article.tag

	related_articles = ArticleModel.objects.filter(tag__tag__icontains=article_tag).exclude(pk=article.pk)[0:3]

	if len(related_articles) < 3:
		related_articles = ArticleModel.objects.all().exclude(pk=article.pk)[0:3]

	return related_articles

@register.simple_tag
def get_category_articles(category):
	category_articles = ArticleModel.objects.all().filter(tag__tag__icontains=category)

	category_articles = category_articles.filter(is_published=True)

	return category_articles