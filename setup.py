from setuptools import setup

setup(name='faa_eval',
      version='0.1',
      description='FAA CFR Title 14 Part 77.9 notice criteria automator.',
      url='https://github.com/kataphraktos/faa_eval',
      author='kataphraktos',
      author_email='67304993+kataphraktos@users.noreply.github.com',
      license='MIT',
      install_requires=[
          'selenium',
          'bs4',
          'requests',
          'six',
          'pillow'
      ],
      zip_safe=False)
