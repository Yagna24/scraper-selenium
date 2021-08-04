# scraper-selenium
Web Scraping using Selenium

                               --------------Steps------------

1. Used chrome webdriver to open the given link.

2. Went to all reviews page and checked number of reviews on every page which was 20. 

3. Collected XPATHS of all required features i.e. Name, Date, Title, Description and Rating. 

4. Added a link.click() to click the next page after every 20 reviews.

5. Created empty list for every feature.

6. Looped through the individual features and appended them to a list.

7. Saved all lists to a dataframe.

8. Exported all lists to csv file. 

      
                           ---------------Problems faced and Solved---------------


1. All had unique xpaths, figured out what part was varying for every feature and iterated through
   it by creating 2 sub xpaths. i.e. path1+x+path2

  x- varying part that would be updated via a for loop.

2. Issue with getting the element by class_name, error said class_name not present, used find_element_by_xpath()
   instead.

