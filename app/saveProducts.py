import htmlget
from bs4 import BeautifulSoup

class getProduct():
    def getProductID(self, URL):
        requestInstance = htmlget.Request()
        htmlText = requestInstance.url(URL)

        soup = BeautifulSoup(htmlText, 'html.parser')
        script_tag = soup.find('script', text=lambda t: t and 'window.CategoryFilteredProducts.push' in t)

        if script_tag:
            content = script_tag.string
            # Extract the desired content from the script tag
            # You can use string manipulation or regular expressions to extract the content

            # Example: Extracting content between parentheses
            start_index = content.index("'") + 1
            end_index = content.rindex("'")
            extracted_content = content[start_index:end_index]

            # Return the extracted content
            return extracted_content
        else:
            return None