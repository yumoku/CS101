from extract_links import extract_link,extract_links_from_single_webpage,read_html_webpage

def crawl_web(web_url: str):
    to_crawl = []
    crawled = []

    crawled.append(web_url)
    to_crawl = extract_links_from_single_webpage(web_url)
    for item in to_crawl:
        if item not in crawled:
            crawled.append(item)
            candidates = extract_links_from_single_webpage(item)

            for candidate in candidates:
                if candidate not in crawled and candidate not in to_crawl:
                    crawled.append(candidate)
                    to_crawl.append(candidate)

    return crawled

def main():
    all_urls = []
    all_urls = crawl_web('http://www.xkcd.com')
    print(all_urls)

if __name__ == "__main__":
    main()
