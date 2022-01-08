from django import template
from ..models import TradingDay

register = template.Library()

@register.simple_tag
def calculate_total_profits(trades):
	total_profits = 0

	for trade in trades:
		total_profits += (trade.exit_price * trade.stock_amount) - (trade.entry_price * trade.stock_amount) - trade.total_commision

	return total_profits

@register.simple_tag
def calculate_day_dev(trade):
	try:
		previous_day = TradingDay.objects.all().filter(trading_date__lt=trade.trading_date).order_by('-trading_date').first()
		day_dev = (trade.end_of_day_balance - previous_day.end_of_day_balance)/previous_day.end_of_day_balance * 100
		return "{:.2f}".format(day_dev)
	except:
		return 0

@register.simple_tag
def get_trades_hit_rate(trading_days):
	winners = 0
	losers = 0

	for trading_day in trading_days:
		for trade in trading_day.trades.all():
			if trade.is_winner == True:
				winners += 1
			else:
				losers += 1

	return [winners, losers]
