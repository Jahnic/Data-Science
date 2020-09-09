import scrape
import pandas as pd 
path = "/usr/local/bin/geckodriver"

df = scrape.get_jobs('data_scientist', 15, False, path, 10)