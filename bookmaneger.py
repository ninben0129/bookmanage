# -*- coding: utf-8 -*-
import requests
import json
import openpyxl
import glob

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
wb = openpyxl.load_workbook("booklist.xlsx")
ws = wb.worksheets[0]
files = glob.glob("./bookpic/*.jpg")


def isbntoinfo(isbn):
    req_url = url + isbn
    response = requests.get(req_url).json()
    # totalitems = response['totalItems']  # 件数
    items_list = response['items']  # items リストデータ
    items = items_list[0]  # items
    info = items['volumeInfo']
    title = info['title']
    author = info['authors'][0]
    publisher = info['publisher']
    publisheddate = info['publishedDate']
    pages = info['pageCount']
    language = info['language']
    print(title)
    print(author)
    print(publisher)
    print(language)


def main():
    isbn_input = input("input ISBN >>>")
    isbntoinfo(isbn_input)


if __name__ == "__main__":
    main()
