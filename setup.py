from distutils.core import setup
setup(
  name = 'jani_text_cleaning',
  packages = ['jani_text_cleaning'],
  version = '0.11',
  license='MIT',
  description = 'This python package does cleaning tasks on textual data and gives tokenized output.',
  author = 'HARSH JANI',
  author_email = 'harshjani53@gmail.com',
  url = 'https://github.com/harshjani53/jani_text_cleaning',
  download_url = 'https://github.com/harshjani53/jani_text_cleaning/archive/refs/tags/0.1.1.tar.gz',   
  install_requires=[
        'pandas','openpyxl','numpy','nltk'
      ])