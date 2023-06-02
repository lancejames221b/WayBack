There is this author, let’s call him John Doe. He used to write regularly for one of our online newspapers. Unfortunately there was a big ownership issue of the newspaper and the website has been scrapped from the internet since 2016ish. I need to find the articles he wrote for that newspaper.

So I went to the Wayback Machine and got like 10,000 plus URLs from that newspaper. The only way to identify the author of the article is to open each URL and check it manually.

I was thinking of writing a script or something to automate the process. Here’s what I am thinking:

1. I can make a list of all the URLs in a CSV file with an identifier such as a number for each URL.
2. The script will open the CSV file and open the URLs one by one.
3. Once a URL is open, it will look at the source code to find the string “John Doe” (because I figured this was the easiest way to check the author name of the author)
4. If the URL contains the string, it will either do a print line of the URL identifier or write it into a notepad document.
5. Then it will move on to the next URL on the list and continue until the last URL has been analyzed.

Do you have any idea how I can go about doing this?

**_ Instructions _**
pip3 install -r requirements.txt
python3 badguyfinder "bad guy's name" urllist.txt results.txt

working example:

python3 badguyfinder.py "Mark Rasch" urllist.txt results.txt
