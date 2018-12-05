from distutils.core import setup

setup(
    name='django-queued-mailer',
    packages=['queued_mailer'],
    version='0.0.1',
    description='Django mail backend uses celery as email message queue',
    author='jar3b',
    author_email='hellotan@live.ru',
    license="MIT license",
    url='https://github.com/jar3b/django-queued-mailer',
    keywords='python2 django email celery',

    requires=['django (>= 1.11)', 'celery (>= 4.1.1)'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
