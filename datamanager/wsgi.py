import os
import sys
import site
from django.core.wsgi import get_wsgi_application

activate_this = 'F:/django/daeha/datamanager/venv/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(), dict(__file__=activate_this))

# 가상환경의 패키지 추가
site.addsitedir('F:/django/daeha/datamanager/venv/Lib/site-packages')
# Add the site-packages of the chosen virtualenv to work with
# site.addsitedir('C:/Users/myuser/Envs/my_application/Lib/site-packages')

# PYTHONPATH에 application directory 추가
path = os.path.abspath(__file__+'/../..')
if path not in sys.path:
    sys.path.append(path)
# # Add the app's directory to the PYTHONPATH
# sys.path.append('F:/django/daeha/datamanager')
# sys.path.append('F:/django/daeha/datamanager/datamanager')
# sys.path.append('F:/django/daeha/datamanager/venv/Lib/site-packages')

# print(sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'datamanager.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datamanager.settings")

application = get_wsgi_application()
