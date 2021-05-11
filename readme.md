# ACCESSING CLAIR CVE DATABASE USING DJANGO .

[Download Postgres](https://www.postgresql.org/download/)

[Download Pgadmin](https://www.pgadmin.org/download/)

[Checkout clair 2.1.6 ](https://github.com/quay/clair/archive/v2.1.6.zip)

[Download Go](https://golang.org/dl/)

## Config Clair

Note:

1. open [main.go file](https://github.com/quay/clair/blob/v2.1.6/cmd/clair/main.go) file and point to your config.yml
   or [already given config.yml](https://github.com/quay/clair/blob/v2.1.6/contrib/k8s/config.yaml)

2. open [already given config.yml](https://github.com/quay/clair/blob/v2.1.6/contrib/k8s/config.yaml) and edit DB
   Details like below

```markdown
source: postgres://username:password@host:port/database?sslmode=disable (config.yml line no 23)
flagConfigPath := flag.String("config", "your edited config yml path", "Load configuration from the specified file.") (
main.go line no 131)
```

## Run Clair

```markdown
go https://github.com/quay/clair/blob/v2.1.6/cmd/clair/main.go
```

## Windows

```markdown
Add postgres bin path into Environment Variable For Windows 
```

## MAC-OSX

```markdown
For latest Version of postgres brew install postgres For Specific Version of Postgres brew install postgres@version
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

## Ubuntu Related Dependencies

```
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

## Install pip for python3  on Ubuntu

```
sudo apt update
sudo apt install python3-pip
pip3 --version
```

## Install pip for python2  on Ubuntu

```
sudo apt update
sudo apt install python-pip
pip3 --version
```

## Django Installation

```markdown
pip3 install -r requirements.txt
```

## Database Inspection

```markdown
python3 manage.py inspectdb > models1.py
```

## Creating Django Specific Tables  in Existing DB

```markdown
python3 manage.py migrate --fake-initial
```

## Creating Super user for Accessing Admin panel

```markdown
python3 manage.py createsuperuser enter username :
enter email:
optional enter password : 
```

## For running Django  Project

```markdown
screen is used for running command as background
1.screen  press enter key

2. python3 manage.py runserver 0.0.0.0:8000 & press enter
```

## Tunnel Forwarding (replace username with your mac username)

```
ssh -D 9999 -L8000:172.18.27.68:8000 username@35.161.14.160
```

## Admin panel URL

```markdown
http://localhost:8000
```

## Enter Superuser user credentials

![Login Admin Panel](static/img/login.png?raw=true "Login")

![View 1](static/img/view1.png?raw=true "View 1")

![View 2](static/img/view2.png?raw=true "View 2")

## Customization (python3.8/site-packages/django/contrib/admin/views/main.py)

```

self.queryset = self.get_queryset(request)
to_be_shown = False
for message in getattr(messages.get_messages(request), '_queued_messages'):
    if message.tags.startswith("cvs"):
        to_be_shown = True
        break
    else:
        continue
if not to_be_shown:
    messages.add_message(request, messages.INFO, 'Query Executed : {}'.format(str(self.queryset.query)), extra_tags='cvs')
self.get_results(request)
if self.is_popup:
    title = gettext('Select %s')
elif self.model_admin.has_change_permission(request):
    title = gettext('Select %s to change')
else:
    title = gettext('Select %s to view')
self.title = title % self.opts.verbose_name
self.pk_attname = self.lookup_opts.pk.attname

```



## Site packages Directory

python3 -m site

## Scp for more Customization

```
scp -r -i cs_team_shncasb.pem /Users/akumars1/Downloads/pem/django_admin_search ubuntu@172.18.68.234:/home/ubuntu/.local/lib/python3.8/site-packages/
or 
sudo cp /home/ubuntu/clair/customize.py /home/ubuntu/.local/lib/python3.8/site-packages/django/contrib/admin/views/main.py

scp -r -i cs_team_shncasb.pem /Users/akumars1/Downloads/pem/django_admin_search/ ubuntu@172.18.68.234:/home/ubuntu/.local/lib/python3.8/site-packages/django_admin_search

sudo cp -r  /home/ubuntu/clair/custom/ /home/ubuntu/.local/lib/python3.8/site-packages/django_admin_search/
```