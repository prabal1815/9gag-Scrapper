Built a scraper
- Scrapes 9gag’s Hot category
- Categorize the content according to Video/GIF/Image
- Store with metadata into a local NoSQL Server like MongoDB
- The scraper runs every 10 minutes


- Query Script - <content_type> <#num>
- Output - Top #num of results of the content type from 9gag (urls of content only)
- Output results with an additional parameter of a tag. 

Example INPUT- <br> 
GIF 30 <br>
VIDEO 20<br>
IMAGE 40<br>
OVERALL 35<br>
IMAGE 20 <tag>