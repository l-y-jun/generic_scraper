HOWTO
-----

   1. Install selenium package(in requirements.txt).
   #. run main.py file with ``python main.py`` commmand.

Function Usage
--------------

   .. code-block:: python

      def getItemList(domain, page_to = 1, browser = "Chrome", main_queries = [], opt_queries = {}):
         pass

   1. domain에 대한 정보는 ``src/domains.json``\에 명시된 목록의 이름을 사용합니다.
   #. page_to 는 탐색할 최대 페이지 번호를 지정합니다.
   #. browser는 총 4가지 중에 선택이 가능합니다.

      - "Edge": 테스트 X
      - "Firefox": 테스트 O
      - "Chrome": 테스트 X
      - "Safari": 테스트 X 

   #. 다음은 ``src/domain.json``\을 참고하여, 필수 쿼리의 목록인 ``main_queries``\를 만들어야 합니다.

      .. code-block:: python

         main_queries = [
             {"name": "q", "value": keyword}, # 검색키워드
             {"name": "listSize", "value": 60}, # 페이지당 아이템수
             {"name": "sorter", "value":"latestAsc"}, # 아이템 정렬기준
             {"name": "page", "value": page_from}, # 첫 대상페이지 번호
         ]

      - 위의 각 요소는 쿼리의 이름과 값인 name, value로 구성되어 ``q=연필&``\와 같은 식으로 URL에 적용됩니다.
      - ``src/domains.json``\에 해당 이름의 쿼리가 ``values``\를 가지고 있을 경우 ``values``\에 해당하는 항목의 값만 사용할 수 있는 옵션임을 의미합니다. 이런 부분을 어길 경우 에러가 발생하며 스크랩이 진행되지 않습니다.

   #. 위처럼 쿼리구성 요소에 대해 구성이 완료되었다면 해당 함수를 실행합니다.

      .. code-block:: python

         items = getItemList(domain, 3, "Firefox", main_queries, opt_queris)

      - 반환한 ``items``\에는 각 아이템이 key:value의 구성으로 List형 데이터로 반환됩니다.

   #. 최종적으로 ``export_to_file``\함수를 사용하여 items목록을 csv파일로 저장할 수 있습니다.

      .. code-block:: python

         export_to_file("ABCD쇼핑몰", "최신신발", items)

      - 여기서의 이름은 파일을 저장하는데에 생성되는 파일명과 관련되는 정보이니 매우 독립적입니다. items항목을 제외하고는 커스텀하여 사용하거나 함수를 직접 수정하여 사용해도 괜찮습니다.

TODO
----

   - #TODO 1: Failed Page Handling.

      - From 1~3 Navigating, if page 2 Fails?

         - Retry

            - Quit browser and Retry
            - Retry After End

         - Notify

   - #TODO 2: Duplicate Page Located Handling

      1. First page got page 3
      #. Second page got page 3(no more page)

         - should Stop

LOGS
----

- #11/main.py/Usage Change becuase of changes from #7 to #10

   :commit: eaa4cfd9df9022133023d7acddf78aaefd4cf670
   :Date:   Tue Jun 24 18:14:45 2025 +0900

      - get Urls from ``urls.createURLs`` function
      - start and quit browser by URLs of above. 

         1. Init Browser
         #. Get JSON Data
         #. Create URLs
         #. For loop by URLs

            #. get Page with URL
            #. scrape Items
            #. save to list
            #. quit browser

         #. save item list to csv file

- #10/export.py/safe string on item name for csv

   :commit: 06b3bf52ac2a6bed159eb7c37c8d0e569a517a3b
   :Date:   Tue Jun 24 18:10:11 2025 +0900

   - Feats

      - Safe string work for product name(add double quote mark on each side) to prevent comma seperate rule violations.

         - FROM: 'my item, super great thing' 
         - TO: '"my item, super great thing"' 

- #9/scarpe.py/Scrape Item Fixed to work properly

   :commit: c1e54cfaa5ad0ab96b6a4ac4791ab55167ecd5db
   :Date:   Tue Jun 24 18:03:36 2025 +0900

   - Feats

      - according to Coupang item selector changed, also changed attribute of element.
      - now Safe string of price ("12,345Won" -> 12345)
      - Still ``None`` on empty data(mainly on review count, rating)

- #8/Search with Browser Stabilization

   :commit: fb5b8fcd478af79d272fd6fcf943905960adc33e
   :Date:   Tue Jun 24 17:58:41 2025 +0900

   - Feats

      - Now wating and closing the browser became clearer.
      - After #7 urls REBUILD, browser locate page and wait, for load and close.

- #7 ~ 7.1/Rebuild URL making Structure

   :commit: a675b85494cebe86fe23c5dbb9d3145d51201d65
   :Date:   Tue Jun 24 14:45:13 2025 +0900

   - Feats

      - ``urls.py``\: now create URLs not only single page url

         - Navigate Each page in discrete, individually.

            1. create url via domain(coup), page_to(target), main_q(main query list), opt_q(optional query list)
            #. make additional URLS base on main_q(page target) til page_to function parameter
            #. returns list of urls to scrap

         - according to this method change, Url functions added
 
            - validateQueries(origin, queries): check whole length of queries

               - validateQuery(origin, query): check each query followed the rules in domains.json(query name and value)

            - changePageNumber(url, page_key, page): change number of page from url

               - "page=23&", 4 -> "page=4&"

            - getPageNumber(url, page_key): get pagenumber from URL string

               - "page=23&" -> "23"

            - getPageNumberIdx(url, page_key): locate the substring location range of page numbers

               - "page=23&" -> (5, 7) from 5th to 7th

- #6/Export to csv file
   :commit: 25cfef321865f81ae2b86e8815bd361e7c14c244
   :Date:   Thu Jun 5 14:40:44 2025 +0900

   - Feats

      - ``export.py``\: export scraped items to csv file.

         - ``export.export_to_file``

            - filename to save can be managed with parameter
            - internally use ``to_csv`` function to convert items to csv data

         - ``export.to_csv``
         
            - make item list to csv rows string

- #5/scrape items with BS4
   :commit c430df659f2230b96b12fadd4961b5ddd9ccc0fb
   :Date:   Tue Jun 3 19:05:34 2025 +0900

   - Feats

      - ``scrape.scrape_items``\: scrape items with BS4 internally uses ``_scrape_item`` per items

         - ``scrape._scrape_item``\: scrape item info with BS4

            - optional content

               - rating
               - review
         
- #4/Navigate with each page
   :commit: 2bc318918311b8887f256256d6674fd69ad0dbfb
   :Date:   Tue Jun 3 17:32:38 2025 +0900

   - Feats

      - Browser Interaction navigate(DEPRECATE)
         - Browser Each page navigate per page

      - default option of page size is set to maximum item count

- #3/Navigation method button to href
   :commit: 1549908c0f50754506cf3fa1b2b6036490b981d9
   :Date:   Tue Jun 3 14:31:20 2025 +0900

- #1/Navigate Each page by GET
   :commit: a777148e82cb31deed59a815f2e8a872151656a9
   :Date:   Sat May 24 12:19:08 2025 +0900

   - Feats

      - run main.py runs searching with browser(firefox)
      - navigates page from page

   - Issues

      - navigating from page 3-4, found error, but some browser didn't.
         - Navigation method should change location based to UI interaction based.

      - search page range(availability) should be considered.

