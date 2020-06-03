# Roulette API Project

This project emulates an API for manage several roulettes and its creation with its corresponding bets

## Instalation

Clone this repository:
```bash
	$ git clone https://github.com/luismedinaeng/roulette_api
```

Run a virtual environment inside the project folder and run it with:
```bash
	$ virtualenv venv
	$ source venv/bin/activate
```

Install the requeriments with:
```bash
	$ pip3 install -r requirements.txt
```

You are ready for run the application!

# Run

In order to run the application, you need to have a redis-server running on your local machine. Make sure the redise-server is listening on port 6379. This is the default port for redis and is the one managed by the application.

Also, the flask api runs on port 5000 by default, so make sure you don't have any application listening on that port.

Run command:
```bash
	$ python3 -m api.app
```

This will allow the app to listening request on localhost, port 5000

You can check your connection with.
```bash
	$ curl http://localhost:5000/
	{
		'status': 'OK'
	}
	$
```

## Build with

	- Redis
	- Flask
	- Python
	- redis for python


## Author

Luis Medina
