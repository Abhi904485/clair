# ACCESSING CLAIR CVE DATABASE USING DJANGO .



[Download Postgres](https://www.postgresql.org/download/)

[Download Pgadmin](https://www.pgadmin.org/download/)

[Checkout clair 2.1.6 ](https://github.com/quay/clair/archive/v2.1.6.zip)

[Download Go](https://golang.org/dl/)

## Config Clair
Note:
1. open [main.go file](https://github.com/quay/clair/blob/v2.1.6/cmd/clair/main.go) file and point to your config.yml or [already given config.yml](https://github.com/quay/clair/blob/v2.1.6/contrib/k8s/config.yaml)

2. open [already given config.yml](https://github.com/quay/clair/blob/v2.1.6/contrib/k8s/config.yaml) and edit DB Details like below 

```markdown
source: postgres://username:password@host:port/database?sslmode=disable (config.yml line no 23)
flagConfigPath := flag.String("config", "your edited config yml path", "Load configuration from the specified file.") (main.go line no 131)
```

## Run Clair

```markdown
go https://github.com/quay/clair/blob/v2.1.6/cmd/clair/main.go
```

##Windows 
```markdown
Add postgres bin path into Environment Variable For Windows 
```

##MAC-OSX
```markdown
For latest Version of postgres 
brew install postgres
For Specific Version of Postgres
brew install postgres@version
```



## Postgres Database Dump

NOTE : Here we are giving database name clair for change edit —dbname="your db name"

```markdown
pg_dump --dbname="clair" --schema='public' --file="dumped.sql" --table=public.feature --table=public.featureversion
--table=public.keyvalue --table=public.layer --table=public."layer_diff_featureversion" --table=public.lock
--table=public.namespace --table=public."schema_migrations" --table=public.vulnerability --table=public."
vulnerability_affects_featureversion" --table=public."vulnerability_fixedin_feature" --table=public."
vulnerability_notification" --format=p --create --clean --if-exists
```

## Postgres Database Restore

```markdown
psql Database name < dumped.sql

For example :
psql clair < clair_dump.sql
```

## Edit settings.py for Database credentials

```markdown
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'clair', # Database name
'USER': '', # Username
'PASSWORD': '', # Password
'HOST': '127.0.0.1',
'PORT': '5432', } }

```

## Django Installation

```markdown
pip3 install django pip3 install psycopg2-binary
```

## Database Inspection

```markdown
python manage.py inspectdb > models.py
```

## Creating Django Specific Tables  in Existing DB

```markdown
python manage.py migrate —fake-initial
```

## Creating Super user for Accessing Admin panel

```markdown
python manage.py createsuperuser enter username :
enter email: optional enter password : 
```

## For running Django  Project

```markdown
python manage.py runserver 
```

## Admin panel URL

```markdown
http://localhost:8000
```

## Enter Superuser user credentials 

![Login Admin Panel](static/img/login.png?raw=true "Login")

![View 1](static/img/view1.png?raw=true "View 1")

![View 2](static/img/view2.png?raw=true "View 2")
