[TOC]

# Anime Link Parser

This tool is to find magnet links from anime download website.

Current support:

* https://share.dmhy.org/
* http://www.btsearch.net/

# Usage

1. Go to website and narrow down search filter
   
   > Something like: "DMG usage S2 big5" (in btsearch site)
   
2. Copy the full url path from browser
   
   > http://www.btsearch.net/DMG%20usagi%20S2%20big5%20-first-asc-1
   
3. Use command line tool to grep the magnet links
   
   ``` bash
   $ python getLink.py http://www.btsearch.net/DMG%20usagi%20S2%20big5%20-first-asc-1
   ```
   
4. Magnet links will also be stored in local file (links.txt)

