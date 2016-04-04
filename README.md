# Python Scraper

The [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
and [Requests](http://docs.python-requests.org/en/master/) modules
must be installed for this script to function.

Program works pretty simply; just clone the repo and run scraper.py
and you will be prompted for a google search term. Some searches will
break the program due to inconsistent link formatting across
different websites.

Try something like 'python is cool'. That seems to work.

The first twenty links will be displayed on the command line as well
as anything contained in a p tag for every link. There might be less
than twenty results if the urls on the page were inconsistent. There
might also be a few cases where there are not any p tags for a given
result. I'm still working on saving both the links and the p tags in
a MySQL database.