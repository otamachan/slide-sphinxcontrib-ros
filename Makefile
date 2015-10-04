all:
	mkdir -p _build
	sphinx-build -b slides . _build/slides
	$(MAKE) -C _sample

clean:
	rm -rf _build *~
