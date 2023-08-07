coldStartHeater.py is a simple solution for overcoming the 15 minute memory
limitation Render.com has for web services that don't get much traffic.
Cold starts on Render could mean around 1 minute of waiting for a simple website.
This application, in its first version, is annoying if you're running it on a
machine you actually use because it opens and closes a browser window every 14
minutes. It is best to run it on something like a raspberry pi if you have one 
hanging around collecting dust.

You will need to install Selenium on your machine. Then you will need to install
a driver specific for the browser(s) you prefer, and your OS. You can find out how
to do both of those here: https://pypi.org/project/selenium/

You will also need to install python-dotenv and create a .env file. This page shows how to do that: 
https://pypi.org/project/python-dotenv/

Add COLD_URL=example.com to your .env file. COLD_URL 
is the web address for the site you wish to keep running without cold starts.