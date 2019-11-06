FROM python:3.6
ADD . /makarenko_blog
ENV DJANGO_SETTINGS_MODULE my_site.settings
RUN pip install -r /makarenko_blog/requirements.txt
CMD python /makarenko_blog/manage.py runserver 0.0.0.0:8000
