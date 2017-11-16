from libcpp.string cimport string

cdef extern from "cpp/src/fasttext.h" namespace "fasttext":
    cdef cppclass FastText:
        FastText()

        void loadModel(string filename)
        string textVector(string text)
