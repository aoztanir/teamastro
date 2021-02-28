import random, string
from flask import Flask, render_template, request

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

ok_chars = string.ascii_letters + string.digits

@app.route('/')  # What happens when the user visits the site
def base_page():

	return render_template(
		'index.html',  # Template file path, starting from the templates folder. 

	)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('/404.html'), 404


@app.route('/astro-is-ready')
def astroReady():
	rand_ammnt = random.randint(10, 100)
	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
	return render_template('/astro-is-ready.html', random_str=random_str)


@app.route('/commands')
def commands():
	rand_ammnt = random.randint(10, 100)
	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
	return render_template('/commandsImage.html', random_str=random_str)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=4000  # Randomly select the port the machine hosts on.
	)