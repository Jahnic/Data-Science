![](centris.jpeg)

# Introduction
While the reasons for homeownership may vary, asset appreciation is a common denominator. Those interested in buying a home will either need to spend a significant time on research or entrust a real estate agent to find the best fit. Because of the large volume and variety of relevant data, manual examinations will inevitably be limited. Many properties with high potential ROIs are likely to be missed. To address this issue, I propose the deployment of a regression model to estimate prices based on several indicators. Deviations from the expected value may reveal underappreciated real estate that can be used as starting points for investors and future homeowners.  

Data is retrieved through web scraping listing from Montreal using `Selenium` on [Centris](https://www.centris.ca/en/properties~for-sale~montreal-island?view=Thumbnail).

# Installation
1. Install required packages: `numpy`, `pandas`, `selenium`
2. Install [Chromedriver](http://chromedriver.chromium.org/). The specified installation path is `'C:/webdriver/chromedriver.exe'`. If you are not using windows you will need to change the path in the code. 
