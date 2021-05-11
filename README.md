# Migrations Workshop - DjangoCon Europe 2021

This is the toy project for DjangoCon Europe 2021, *Migrations Workshop*.
The complete title is *Migrations and understanding Django's relationship with its database*.
and will take place 2021-06-04 from 09:45 to 10:35 (UTC+2). See https://cfp.2021.djangocon.eu/2021/talk/VHFEDF/

## For the workshop, please install this project using these steps

This is repository contains a fresh Django project, with one view, one URL, one template and one model.
During the workshop, we will edit the model to explore some aspects of Django Migrations.

1. **Clone the repository**

For instance: `git clone git@github.com:David-Wobrock/djangocon-europe-2021-migrations-workshop.git`

2. **Choose the relational database you are familiar with**

Preferably MySQL or PostgreSQL. I will use PostgreSQL during the workshop.
Avoid relying on sqlite for the workshop, we will talk about it during the session :)

3. **Configure your database**

Set up the database management system, and be aware of the username and password to connect to it.
And already create a database called `djangocon_migrations_workshop`.

4. **Install Python libraries**

The latest Django will do just fine, and you might need to install a driver for the chosen database.
If you use MySQL, you will need `mysqlclient`. If you use PostgreSQL, you will need `psycopg2`.

For instance: `pip install django psycopg2`

5. **Configure the Django project to use your database**

Edit the `DATABASES` configuration in the Django project settings to make it use the credentials configured in step 3.
You only need to edit the configuration for the `default` database.

See https://github.com/David-Wobrock/djangocon-europe-2021-migrations-workshop/blob/main/migrations_workshop/settings.py#L78-L84

6. **Make sure everything works**

Run `python manage.py migrate` and ensure that you get many lines that end with `... OK`.

Run `python manage.py runserver` and ensure you can access the homepage saying *The install worked successfully!*.

We should be ready to roll now! See you then!
