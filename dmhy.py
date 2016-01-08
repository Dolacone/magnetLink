import urllib2
from lxml.html.clean import Cleaner
from lxml import etree
from StringIO import StringIO
import json
import sys

outputFile = open('pageResult.txt', 'w')

def output(outString, fp=None):
  if type(outString) == dict:
    outString = json.dumps(outString)
  if fp:
    fp.write(outString.encode('utf-8') + '\r\n')
  print(outString)

def getPage(url):
  browserHeader = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
  }
  urlRequest = urllib2.Request(url, headers=browserHeader)
  pageContent = urllib2.urlopen(urlRequest).fp.read()
  return pageContent

def parseEtree(htmlContent):
  cleaner_args = {
    "javascript": True,
    "page_structure": True,
    "style": True
  }
  cleaner = Cleaner(**cleaner_args)
  htmlContent = cleaner.clean_html(htmlContent)
  return etree.parse(StringIO(htmlContent), etree.HTMLParser())

def parseResultTitle(searchItem):
  return ''.join(searchItem.xpath('./td[@class="title"]/a/text()'))

def parseMagnetLink(searchItem):
  return searchItem.xpath('./td/a[@class="download-arrow arrow-magnet"]/@href')[0]

def parseResult(tree):
  for resultItem in tree.xpath('//div[@class="table clear"]//tbody/tr'):
    output(parseResultTitle(resultItem), outputFile)
    output(parseMagnetLink(resultItem), outputFile)

  