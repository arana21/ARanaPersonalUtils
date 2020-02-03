from setuptools import setup

setup(name='ARanaPersonalUtils',
      version='0.1',
      description='Personal Util files',
      url='https://github.com/arana21/ARanaPersonalUtils',
      author='A. Rana',
      author_email='amanrana20@icloud.com',
      license='MIT',
      packages=['bin', 'src'],
      dependencies=[
          'flake8',
          'black',
          'pylint',
          'numpy',
          'io',
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],)
