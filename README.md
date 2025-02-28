![Logo of the project](https://i.imgur.com/6D52noG.png)

# News Agency
> A system for tracking newspaper editors

You can view the deployed project at [News Agency](https://news-agency-60j2.onrender.com/) and log in with the following test user credentials:  
**Login:** `user`  
**Password:** `user12345`

News Agency is a system designed to track the editors responsible for each issue of a newspaper. It enhances transparency, accountability, and workflow efficiency by ensuring that every edition has a clear editorial record. With News Agency, managing and reviewing newspaper editions becomes more organized and reliable.

## Installing / Getting started

To get started with News Agency, follow these simple steps to set up the project and run a basic example.

```shell
git clone https://github.com/EugeneDolinskiy/news-agency.git
cd news-agency
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
> **Note**: Before using the service, you must create a superuser with `python manage.py createsuperuser`, as user registration has not been implemented yet.

Once the server is running, open your browser and go to http://127.0.0.1:8000/ to access the system.

### Initial Configuration

Some projects require initial configuration (e.g. access tokens or keys, environment variables, or dependencies). Ensure you have the necessary settings in your `.env` file or `settings.py` before running the project.

## Developing

Here's a brief intro about what a developer must do in order to start developing the project further:

```shell
git clone https://github.com/EugeneDolinskiy/news-agency.git
cd news-agency
pip install -r requirements.txt
```

Make your changes, commit, and create a pull request to contribute.

### Building

If your project needs some additional steps for the developer to build the project after some code changes, state them here:

```shell
python manage.py collectstatic
```

This command collects all static files into the appropriate directory for deployment.

### Deploying / Publishing

To deploy the project, follow these steps:

```shell
git push origin main
```

This pushes the latest changes to the repository for deployment.

## Features

- Track newspaper editors responsible for each issue
- Maintain transparency and accountability
- Easy-to-use interface for managing newspaper issues

## Configuration

Some configurations that users can modify:

#### `DEBUG`
Type: `Boolean`  
Default: `True`

Set to `False` in production to disable debugging features.

#### `DATABASE_URL`
Type: `String`  
Default: `SQLite (db.sqlite3)`

Specify a PostgreSQL, MySQL, or other database URL for production use.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Links

- Repository: [GitHub](https://github.com/EugeneDolinskiy/news-agency)
- Issue tracker: [GitHub Issues](https://github.com/EugeneDolinskiy/news-agency/issues)

## Licensing

The code in this project is licensed under the MIT license.