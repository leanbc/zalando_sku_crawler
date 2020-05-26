# Zalando Skus Crawler
Just replace in config.ini the URL and the path to your local machine where you want to 
put the csv with the Sku data.

After that, run from the root of the repo:

1 - ```pip install -r ./requirements.txt```
2 - ```python3 skus_crawler.py```

If you do not want to install python, the script is runable in Docker Container.You need to have installed Make and
Docker. Run then from the root of the repo:

1- ```make run_crawler```