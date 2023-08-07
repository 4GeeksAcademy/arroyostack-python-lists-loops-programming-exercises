all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_color(color):
    return True if color["sexy"] == True else False

def generate_html(color):
    html_element = f"<li>{color['label']}</li>"
    return html_element

filtered_color = list(filter(filter_color, all_colors))

color_html = list(map(generate_html, filtered_color))

print(color_html)

