document.addEventListener('DOMContentLoaded', function() {
	StartInterval()
});

function StartInterval() {
	var quote_container = document.getElementById('home-page-quote-container');
	var quote_element = document.getElementById('home-page-investment-quote');
	var quote_author_element = document.getElementById('home-page-investment-quote-author');
	var increase_speed = -0.005;
	var is_increasing = false;
	var is_paused = false;

	setInterval(function() {
		if (is_paused == false) {
			if (is_increasing == true) {
				if (parseFloat(quote_container.style.opacity) < 0.99) {
					quote_container.style.opacity = String(parseFloat(quote_container.style.opacity) + increase_speed);
				}else {
					is_paused = true;
					quote_container.style.opacity = '1';
					increase_speed = increase_speed * -1;
					is_increasing = false;
					setTimeout(function() {
						is_paused = false;
					}, 10000);
				}
			}

			if (is_increasing == false) {
				if (parseFloat(quote_container.style.opacity) > 0.01) {
					quote_container.style.opacity = String(parseFloat(quote_container.style.opacity) + increase_speed);
				}else {
					is_paused = true;
					quote_container.style.opacity = '0';
					increase_speed = increase_speed * -1;
					is_increasing = true;
					$.get('investment_quotes', function(response) {
						data = response['data'];
						random_data_item = Math.floor(Math.random() * data.length);
						quote_element.innerHTML = '"' + data[random_data_item]['quote'] + '"';
						quote_author_element.innerHTML = data[random_data_item]['author'];
					});
					setTimeout(function() {
						is_paused = false;
					}, 500);
				}
			}
		}
	}, 10);
}