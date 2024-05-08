import pyshorteners

url = input("Enter the URL: ")

print("Shortened URL: ", pyshorteners.Shortener().tinyurl.short(url))