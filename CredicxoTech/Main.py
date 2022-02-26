# importing libraries
from bs4 import BeautifulSoup
import requests
import html5lib

def main(URL):
	# open our output file in append mode
	File = open("out.csv", "a")

	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
				
	# Making the HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# retrieving product title
	try:
		# Outer Tag Object
		title = soup.find("span",attrs={"id": 'productTitle'})
						

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip().replace(',', '')

	except AttributeError:
		title_string = "NA"
	print("product Title = ", title_string)

	# saving the title in the file
	File.write(f"{title_string},")

	# retrieving price
	try:
		price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
			
								
	except AttributeError:
		price = "NA"
	print("Products price = ", price)

	# saving
	File.write(f"{price},")

	# product img
	
	try:
		images = soup.findAll('img')
		example = images[0]
	except AttributeError:
		example = NA

	print("Img url", example)
		
	
	File.write(f"{example},")

	# print product details
	try:
		details = soup.find("div", attrs={'id': 'availability'})
		details = details.find("span").string.strip().replace(',', '')
					

	except AttributeError:
		details = "NA"
	print("Details = ", details)

	# saving the details 
	File.write(f"{details},\n")

	# closing the file
	File.close()


if __name__ == '__main__':
# opening our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		main(links)
