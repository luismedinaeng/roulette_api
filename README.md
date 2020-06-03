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

In order to run the application, you need to have a redis-server running on your local machine. Make sure the redise-server is listening on port defined on your configuration file. You can find a sample of it at [db](/db). This is the default port for redis. You can change the host, port and database used by the application setting up the environ with `ROULETTE_DB_HOST`, `ROULETTE_DB_PORT` and `ROULETTE_DB`

Running `redis-server`
```
	$ redis-server db/redis_db.conf
```

Also, the flask api runs on port `5000` by default, so make sure you don't have any application listening on that port. If you want to change the host and port of the api, you can setting up the environ with `ROULETTE_API_HOST` and `ROULETTE_API_PORT`

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
