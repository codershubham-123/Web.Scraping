* First collect URLs of the pages where we want to extract data from.
* Setting up the environment
* We will install libraries using pip:
  pip install requests
  pip install html5lib
  pip install bs4
  pip install lxml
* In order to work with the  html, we will have to get the HTML as a string.
* Then write the code.
* The next step then will be to parse the HTML content and give it a tree like structure so that it can be traversed.
* Once the HTML is fetched using requests as an string, we need to parse it.
* For parsing, we will use python's BeautifulSoup module which will create a tree like structure for our DOM.
* Once the HTML is fetched and parsed, the next step is to manipulate the tree using BeautifulSoup's functions to get our job done.
* Run the code and extract the data.
* Store the data in the csv file.