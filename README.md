# FLASK API PYTHON Boilerplate

<div>
  Created by BitByBit team and maintained with ❤️ by an amazing <a href="https://www.hackerearth.com/challenges/hackathon/airbus-aerothon-40-finale/dashboard/1bfeeee/team/">team of developers</a>.
</div><br />

## Prerequisite

- Python 3.7 or above  : Installation instructions can be found [here.](https://docs.python.org/3/using/index.html)
- Flask Package Download v1.x or above. Installation instructions can be found [here.](https://flask.palletsprojects.com/en/2.1.x/installation/)

## Available Scripts

To start with the project, run below command to install the project:

### go on app.py file and right click to run

Now your application is ready to run. Run below command to run app in developement mode.

### `run server`

Open [http://localhost:5000](http://localhost:5000) to view it in your browser.

The page will reload when you make changes.\
You may also see any errors in the console.

## To deploy the application

Prerequisite - Python, FLASK, docs can be found [here.](https://docs.python.org/3/using/index.html)(https://flask.palletsprojects.com/en/2.1.x/installation/)


### Start an application

You can start application by simply using :run command through right click on app.py file.

Your app is now daemonized, monitored and kept alive forever.

### Managing Applications

Once applications are started you can manage them easily:


Managing apps is straightforward:

`stop can be possible by button click which will terminate the current ` \
`re-run can be used for terminating first current deployment and restart the process again, app will run `\

### [Config module]

You can store configuration secrets, passwors or keys in `config.py` file. Sample variables added to `static/Files/config.py` for reference. To access any of variable across the application use below code:

`app.config.update(TESTING=True,SECRET_KEY=#secret_key_from_config_file')` 