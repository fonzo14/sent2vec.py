clean:
	rm -f -r build/
	rm -f *.so

clean-cpp:
	rm -f sent2vec/sent2vec.cpp

clean-all: clean clean-cpp

.PHONY: build
build: clean
		   python setup.py build_ext --inplace
