import glob
from setuptools import setup, find_packages

setup(name='pagico',
      version='0.5.0',
      description='Pagico for Linux',
      author='Tualatrix Chou',  
      author_email='tualatrix@gmail.com',
      url='http://www.pagico.com/',
      scripts=['pagico-client', 'pagico-helper'],
      packages=find_packages(),
      data_files=[
          ('../etc/dbus-1/system.d/', ['data/pagico-daemon.conf']),
          ('share/dbus-1/system-services', ['data/com.pagico.daemon.service']),
          ('../opt/pagico/', ['pagico-daemon', 'splash.png']),
          ('../lib32/', ['libgd.so.2']),
          ],
      license='GNU GPL',
      platforms='linux',
      test_suite='tests',
)