import requests
from bs4 import BeautifulSoup
import sys

def scrape_and_check(url):
    # Send a request to fetch the HTML content of the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        sys.exit(1)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element matching the given selector
    target_element = soup.select_one('body > div.container > main > section.showtimes > p')

    # Check if the target element exists and contains the text "No"
    if target_element and "No" in target_element.text:
        print("Bookings at friday are not available yet.")
        sys.exit(0)
    else:
        print("Bookings at friday are available!.")
        sys.exit(1)

if __name__ == "__main__":
    url = "https://egy.voxcinemas.com/showtimes?c=city-centre-almaza&m=oppenheimer&d=20230728"
    scrape_and_check(url)
