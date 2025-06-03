HOWTO
-----

   1. Install selenium package(in requirements.txt).
   #. run main.py file with ``python main.py`` commmand.

TODO
----

   - Scraped items save to CSV file output

LOGS
----

4. #5/scrape items with BS4
   :commit c430df659f2230b96b12fadd4961b5ddd9ccc0fb
   :Date:   Tue Jun 3 19:05:34 2025 +0900

   -Feats

      - ``scrape.scrape_items``\: scrape items with BS4 internally uses ``_scrape_item`` per items

         - ``scrape._scrape_item``\: scrape item info with BS4

            - optional content

               - rating
               - review
         
3. #4/Navigate with each page
   :commit: 2bc318918311b8887f256256d6674fd69ad0dbfb
   :Date:   Tue Jun 3 17:32:38 2025 +0900

   - Feats

      - Browser Interaction navigate(DEPRECATE)
         - Browser Each page navigate per page

      - default option of page size is set to maximum item count

2. #3/Navigation method button to href
   :commit: 1549908c0f50754506cf3fa1b2b6036490b981d9
   :Date:   Tue Jun 3 14:31:20 2025 +0900

1. #1/Navigate Each page by GET
   :commit: a777148e82cb31deed59a815f2e8a872151656a9
   :Date:   Sat May 24 12:19:08 2025 +0900

   - Feats

      - run main.py runs searching with browser(firefox)
      - navigates page from page

   - Issues

      - navigating from page 3-4, found error, but some browser didn't.
         - Navigation method should change location based to UI interaction based.

      - search page range(availability) should be considered.


