import os
import builtins

from interface cimport FastText

cdef class FastTextWrapper:
  cdef FastText* _ft
  def __cinit__(self):
    self._ft = new FastText()
  def __dealloc__(self):
    del self._ft
  def load_model(self, filename, encoding='utf-8'):
    self._ft.loadModel(builtins.bytes(filename, encoding))
  def text2vec(self, text, encoding='utf-8'):
    vec = self._ft.textVector(builtins.bytes(text, encoding))
    return str(vec, encoding).strip()

def load_model(filename):
  if not os.path.isfile(filename):
    raise ValueError("fastText/sent2vec: trained model %s cannot be opened!" % filename)

  ft = FastTextWrapper()
  ft.load_model(filename)

  return ft
