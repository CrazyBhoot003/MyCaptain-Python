import requests
from bs4 import BeautifulSoup

oyo_url = "https://www.oyorooms.com/search?location=Delhi%2C%20India&city=Delhi&searchType=city&coupon=&checkin=05%2F01%2F2021&checkout=06%2F01%2F2021&roomConfig%5B%5D=1&showSearchElements=false&guests=1&rooms=1&countryName=India&country=india&filters%5Bcity_id%5D=2"

req = requests.get(oyo_url)
content =req.content

soup = BeautifulSoup(content, "html.parser")
print(soup)
all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
for hotel in all_hotels:
    hotel_name = hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
    print(hotel_name) 