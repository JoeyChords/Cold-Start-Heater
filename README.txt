coldStartHeater.py is a simple solution for overcoming the 15 minute memory
limitation Render.com has for web services that don't get much traffic.
Cold starts on Render could mean around 1 minute of waiting for a simple website.
This application, in its first version, is annoying if you're running it on a
machine you actually use because it opens and closes a browser window every 14
minutes. It is best to run it on a dedicated machine for running annoying tasks.

Create a .env file and add COLD_URL=example.com, replacing example.com with the web 
address for the site you wish to keep running without cold starts.

Install requirements from requirements.txt.

You will need to install Selenium on your machine. Selenium's built-in driver manager 
should install the driver you need for your browser automatically, but you may need to 
install a driver specific for the browser(s) you prefer, and your OS. You can find out how
to do both of those here: https://pypi.org/project/selenium/

You will also need to install python-dotenv. This page shows how to 
do that: https://pypi.org/project/python-dotenv/

