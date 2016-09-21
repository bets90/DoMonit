from setuptools import setup

setup(name='domonit',
      version='0.1',
      description='Docker monitoring API wrapper for python scripts',
      url='https://github.com/bets90/DoMonit',
      author='Betselot Abebe',
      author_email='betselot@student.chalmers.se',
      license='MIT',
      packages=['domonit', 'utils'],
      zip_safe=False)