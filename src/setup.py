from setuptools import setup, find_packages


tests_require = [
    [
        "colorama==0.3.9",
        "coverage==4.5.1",
        "django-nose==1.4.5",
        "nose==1.3.7",
        "pinocchio==0.4.2",
    ]
]

setup(
    name="todobackend",
    version="0.1.0",
    description="Todobackend Django REST service",
    packages=find_packages(),
    include_package_data=True,
    scripts=["manage.py"],
    install_requires=[
        "django==1.11.5",
        "django-cors-headers==2.4.0",
        "djangorestframework==3.8.2",
        "psycopg2==2.7.3.1",
    ],
    tests_require=tests_require,
    extras_require={
        "test": tests_require
    },
)
