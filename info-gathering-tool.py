# Import necessary modules
import whois
import dns.resolver
import shodan
import requests 
import argparse

# Create an ArgumentParser object for handling command-line arguments
argparse = argparse.ArgumentParser(description="Information Gathering tool.", usage="python3 info_gathering.py -d DOMAIN [-s IP]")

# Add arguments to the ArgumentParser object
argparse.add_argument("-d", "--domain", help="Enter the Domain name for Footprinting.")
argparse.add_argument("-s", "--shodan", help="Enter the IP for Shodan search")

# Parse the command-line arguments
args = argparse.parse_args()

# Extract domain and IP from the parsed arguments
domain = args.domain
ip = args.shodan

# Print the domain and IP
print("[+] Domain {} and IP {}".format(domain, ip))

# Here you could add more functionality like performing whois lookup, DNS resolution, Shodan search, etc.
# For example:
# - Perform whois lookup
# whois_info = whois.whois(domain)
# print(whois_info)

# - Perform DNS resolution
# try:
#     dns_result = dns.resolver.resolve(domain, 'A')
#     for ip in dns_result:
#         print(ip)
# except dns.resolver.NXDOMAIN:
#     print("Domain does not exist.")
# except dns.resolver.NoAnswer:
#     print("No A record found for the domain.")

# - Perform Shodan search
# api_key = 'YOUR_SHODAN_API_KEY'
# api = shodan.Shodan(api_key)
# try:
#     results = api.search(ip)
#     for result in results['matches']:
#         print(result)
# except shodan.APIError as e:
#     print('Error: {}'.format(e))
