from django.db import models
from django.template.defaultfilters import slugify 
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import datetime
from django.contrib import admin

# Create your models here.
class InvestmentQuoteModel(models.Model):
	author = models.CharField(max_length=24)
	quote = models.TextField(max_length=256)
	auto_increment_id = models.AutoField(primary_key=True)

	def __str__(self):
		return f'({self.auto_increment_id}) by {self.author}'

class TagModel(models.Model):
	tag = models.CharField(max_length=24)

	def __str__(self):
		return self.tag

class ArticleModel(models.Model):
	article_header = models.CharField(max_length=256)
	article_content = models.TextField(null=True, blank=True)
	article_resume = models.TextField(null=True, blank=True)
	article_date = models.DateField(editable=False, null=True, blank=True)
	article_last_updated = models.DateTimeField(editable=False, null=True, blank=True)
	article_slug = models.SlugField(editable=False, unique=True, blank=True, null=True)
	auto_id = models.AutoField(primary_key=True)
	article_cover_art = models.FileField(null=True, blank=True)
	tag = models.ForeignKey(TagModel, on_delete=models.CASCADE, blank=True, null=True)
	is_published = models.BooleanField(default=False)
	is_created = models.BooleanField(default=False, editable=False)
	read_count = models.IntegerField(default=0, editable=True)

	def __str__(self):
		return str(self.article_header)

@receiver(pre_save, sender=ArticleModel)
def save_article_slug(sender, instance, *args, **kwargs):
	instance.article_last_updated = datetime.datetime.now()

	if instance.is_created == True:
		instance.article_slug = slugify(instance.article_header + "-" + str(instance.auto_id))

@receiver(post_save, sender=ArticleModel)
def set_unique_slug(sender, instance, created, *args, **kwargs):
	if created:
		instance.article_date = datetime.date.today()
		instance.article_slug = slugify(instance.article_header + "-" + str(instance.auto_id))
		instance.is_created = True
		instance.save()

class TradingDay(models.Model):
	trading_date = models.DateField(blank=False, null=False, unique=True)
	end_of_day_balance = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=10, default=15.000)
	note =  models.TextField(default="")

	def __str__(self):
		return str(self.trading_date)

class TradeModel(models.Model):
	stock_quote = models.CharField(max_length=12, null=False, blank=False)
	stock = models.CharField(max_length=24, null=False, blank=False)
	stock_amount = models.PositiveIntegerField(null=False, blank=False)
	entry_price = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False)
	exit_price = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False)
	total_commision = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False)
	profit_loss = models.DecimalField(editable=False, null=True, blank=True, decimal_places=2, max_digits=12)
	is_winner = models.BooleanField(editable=False, null=True, blank=True)
	trading_day = models.ForeignKey(TradingDay, on_delete=models.CASCADE, related_name='trades')

	def __str__(self):
		return str(self.stock_quote + ": " + self.stock)

@receiver(pre_save, sender=TradeModel)
def set_trade_pl(sender, instance, *args, **kwargs):
	instance.profit_loss = float("{:.2f}".format((instance.exit_price * instance.stock_amount) - (instance.entry_price * instance.stock_amount) - instance.total_commision))

	if instance.profit_loss >= 0:
		instance.is_winner = True
	else:
		instance.is_winner = False








