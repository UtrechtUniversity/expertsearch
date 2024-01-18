# Document- and candidate centric expert search
This page contains the source code and questionnaire that were created for the CHIIR 2024 paper "Improving expert search effectiveness: Comparing ways to rank and present search results"

This work is licensed under a Creative Commons Attribution International 4.0 License.


Disclaimer: 
The code was shared for the purpose of transparency, but it was not rewritten for easy re-usability. The code is fairly messy. In the code we removed individual results (logs, answers questionnaire) we only obtained informed consent for sharing aggregated results.

We do not provide the XML iBabs dump we used, although everything is based on the open data available through https://zoek.openraadsinformatie.nl. We do not include the answers participants provided, as our informed consent form said we would only share results in aggregate


There are five main components:
* Elasticsearch
* Parsing and indexing the iBabs data into elastic
* The interface
* The webserver that connects the interface and elastic
* The file analysing log results (analogs.py)


Main steps to run:

pip install django django-cors-headers elasticsearch_dsl

To run, go to /webserver and run 
	python manage.py runserver
	
To visit site, then open /interface/google-search.html

Make sure elasticsearch.bat is running to enable search

Most logic of the webserver (e.g. talking with the Elastic instance) is in /webserver/queryme/query.py

