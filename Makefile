run_crawler: _run_crawler


DOCKER_IMAGE=centos/python-36-centos7
CURRENT_DIR_NAME:=`pwd | xargs basename`


_run_crawler: 
	( \
	docker run -it --rm \
	-w /$(CURRENT_DIR_NAME) \
	-v `pwd`:/$(CURRENT_DIR_NAME) \
	$(DOCKER_IMAGE) \
	bash -c "pip install -r ./requirements.txt && python skus_crawler.py" \
	)