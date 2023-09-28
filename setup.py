from distutils.core import setup
setup(
  name = 'jani_text_cleaning',
  packages = ['jani_text_cleaning'],
  package_dir={'jani_text_cleaning': 'src/mypkg'},
  package_data={'jani_text_cleaning': ['cleaning/*.py']},
  version = 'v0.0.1',
  license='MIT',
  description = 'This python package does cleaning tasks on textual data and gives tokenized output.',
  author = 'HARSH JANI',
  author_email = 'harshjani53@gmail.com',
  url = 'https://github.com/harshjani53/jani_text_cleaning',
  download_url = 'https://github.com/harshjani53/jani_text_cleaning/archive/refs/tags/v0.0.1.tar.gz',   
  install_requires=[
        'pandas','openpyxl','numpy','nltk'
      ])