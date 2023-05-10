APP_NAME = "Exarth Boiler Plate"
APP_VERSION = "1.0"
APP_DESC = "A boiler plate ready-to-start application for django developers with all basic settings are configured"
APP_CONTACT = "support@exarth.com"
APP_URL = "https://exarth.com/"
APP_TERMS = "https://exarth.com/terms-of-use/"
APP_POLICY = "https://exarth.com/privacy-policy/"
APP_GIT = "https://github.com/IkramKhan-DevOps/"
APP_LICENSE = "MIT License"
APP_ENV = """

ENV FILE CONFIGURATIONS
-----------------------
ENVIRONMENT=local
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_HOST=localhost
DB_USER=thestaffmanagerdbrootuser
DB_PASS=thestaffmanagerdbrootuserpassword
DB_NAME=thestaffmanagerdb
DB_PORT=django.db.backends.postgresql_psycopg2
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=youremail@server.com
EMAIL_HOST_PASSWORD=youremailpassword
EMAIL_PORT=587
BASE_URL=http://127.0.0.1:8000
DEFAULT_FROM_EMAIL=Support-Team <youremail@server.com>
DEBUG=True
SECRET_KEY=YUwsjlxk30PYf6dovmiUK8c0i1MARKIiejYh7kSDv3fiBq2mlWmeXap
TIME_ZONE=Asia/Karachi
GOOGLE_CALLBACK_URL=http://127.0.0.1:8000/accounts/google/login/callback/
ALLOWED_HOST=127.0.0.1
SITE_ID=1
"""

"""
ENV FILE CONFIGURATIONS FOR DOCKER COMPOSE
-----------------------------------------
POSTGRES_DB=wordcountly
POSTGRES_USER=wordcountly123
POSTGRES_PASSWORD=wordcountly@123
SQL_HOST=db
SQL_PORT=5432
ENVIRONMENT=server
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=youremail@server.com
EMAIL_HOST_PASSWORD=youremailpassword
EMAIL_PORT=587
BASE_URL=http://127.0.0.1:8000
DEFAULT_FROM_EMAIL=Support-Team <youremail@server.com>
DEBUG=False
SECRET_KEY=YUwsjlxk30PYf6dovmiUK8c0i1MARKIiejYh7kSDv3fiBq2mlWmeXap
TIME_ZONE=Asia/Karachi
GOOGLE_CALLBACK_URL=http://127.0.0.1:8000/accounts/google/login/callback/
ALLOWED_HOST=127.0.0.1
SITE_ID=1
POSTGRES_DB=hello_django_dev
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
VIRTUAL_HOST=wordcountly.com
VIRTUAL_PORT=8000
LETSENCRYPT_HOST=wordcountly.com

"""
"""
ENV FILE CONFIGURATIONS FOR NGINX PROXY
-----------------------------------------
DEFAULT_EMAIL=wordcountly@wordcountly.com
NGINX_PROXY_CONTAINER=nginx-proxy
"""
