import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'passlib',
    'paginate',  # pagination helpers
    'paginate_sqlalchemy',

    'future',
    'psycopg2',
    'markdown',
    'wtforms',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'tox',
]

dev_requires = ['ipython', 'pyramid-ipython']

setup(name='blog',
      version='0.0',
      description='blog',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Hannah Krager',
      author_email='hannahkrager@gmail.com',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'test': tests_require,
          'dev': dev_requires,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = blog:main
      [console_scripts]
      initialize_db = blog.scripts.initializedb:main
      """,
      )
