from setuptools import setup, find_packages
from setuptools.extension import Extension
from sys import platform

cython = True

try:
  from Cython.Build import cythonize
  cython = True
except ImportError:
  cython = False

# Define the C++ extension
if platform == "darwin":
    extra_compile_args = ['-O3', '-pthread', '-funroll-loops', '-std=c++0x', '-stdlib=libc++', '-mmacosx-version-min=10.7']
else:
    extra_compile_args = ['-O3', '-pthread', '-funroll-loops', '-std=c++0x']

extensions = []

if cython:
  extensions = [
    Extension('*',
      sources=[
        'sent2vec/sent2vec.pyx',
        'sent2vec/cpp/src/args.cc',
        'sent2vec/cpp/src/dictionary.cc',
        'sent2vec/cpp/src/fasttext.cc',
        'sent2vec/cpp/src/main.cc',
        'sent2vec/cpp/src/matrix.cc',
        'sent2vec/cpp/src/model.cc',
        'sent2vec/cpp/src/productquantizer.cc',
        'sent2vec/cpp/src/qmatrix.cc',
        'sent2vec/cpp/src/utils.cc',
        'sent2vec/cpp/src/vector.cc'
      ],
      language='c++',
      extra_compile_args=extra_compile_args
    )
  ]

  extensions = cythonize(extensions)
else:
  extensions = [
    Extension('*',
      sources=[
        'sent2vec/sent2vec.cpp',
        'sent2vec/cpp/src/args.cc',
        'sent2vec/cpp/src/dictionary.cc',
        'sent2vec/cpp/src/fasttext.cc',
        'sent2vec/cpp/src/main.cc',
        'sent2vec/cpp/src/matrix.cc',
        'sent2vec/cpp/src/model.cc',
        'sent2vec/cpp/src/productquantizer.cc',
        'sent2vec/cpp/src/qmatrix.cc',
        'sent2vec/cpp/src/utils.cc',
        'sent2vec/cpp/src/vector.cc'
      ],
      language='c++',
      extra_compile_args=extra_compile_args
    )
  ]

# Package details
setup(
  name='sent2vec',
  version='0.1.0',
  author='',
  author_email='',
  url='',
  description='A Python interface for sent2vec library',
  license='BSD 3-Clause License',
  packages=['sent2vec'],
  ext_modules = extensions,
  install_requires=[],
  classifiers= []
)
