import asyncio
import aiohttp
import sys
from bs4 import BeautifulSoup

# get the search string from command line argument
search_string = sys.argv[1]

# open the input file and read all the URLs into a list
input_file = sys.argv[2]
with open(input_file, 'r') as file:
    urls = file.read().splitlines()

# open the output file to write successful URLs
output_file = sys.argv[3]
out_file = open(output_file, 'w')

async def check_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_content = await response.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            if search_string.lower() in soup.get_text().lower():
                out_file.write(f"{url}\n")
                print(f"Article written by {search_string} found in URL {url}")

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(check_url(url)))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    out_file.close()


#python3 check_urls.py <search string> <input urls file name> <output file name>