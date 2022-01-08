from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(InvestmentQuoteModel)
admin.site.register(ArticleModel)
admin.site.register(TagModel)

class TradeModelInLineAdmin(admin.TabularInline):
	model = TradeModel
	min_num = 0
	extra = 0

class TradingDayAdmin(admin.ModelAdmin):
	inlines = [TradeModelInLineAdmin]

	def get_queryset(self, request):
		queryset = super(TradingDayAdmin, self).get_queryset(request)

		queryset = queryset.order_by('-trading_date')

		return queryset

admin.site.register(TradingDay, TradingDayAdmin)


"""
class BookInLineAdmin(admin.TabularInline):
	model = Book
	min_num = 0
	extra = 0
	can_delete = True
	fields = ['title']

class AuthorAdmin(admin.ModelAdmin):
	inlines = [BookInLineAdmin]

admin.site.register(Author, AuthorAdmin)
"""