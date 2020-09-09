import scraper 
import pandas as pd 
path = "/usr/local/bin/geckodriver"

keywords = "data AND (scientist OR engineer OR analyst)"
df = scraper.get_jobs(keywords, 15, False, path, 5)

df