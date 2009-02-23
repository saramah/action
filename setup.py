try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name="action",
    version="0.1",
    description="personal organizer",
    author="Sarah G Barbour",
    author_email="sarah@radian.org",
    url="http://aladysprimer.net",
    install_requires=["Pylons>=0.9.6.1", "SQLAlchemy>=0.4.1"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'action': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'action': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = action.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
