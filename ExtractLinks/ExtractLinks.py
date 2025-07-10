import requests

def extract_link(text: str):
    """
    This method is to find the beginning index
    and ending index of a web url
    :param text: target text to be searched
    :return: the indexes and new string removed the web url
    """
    target_string = "<a href="
    target_sign = "\""
    anchor = text.find(target_string)
    begining = anchor + len('<a href="')
    end = text.find(target_sign,begining + 1)
    url = text[begining:end]

    return url, end

def read_html_webpage(web_url):
    """
    Read the contents of a webpage and modify
    the link url to absolute link url, also
    adjust the protocol-relative URL
    """
    source = requests.get(web_url).text
    # some links are using protocol-relative URLs
    # such as //c.xkcd.com/random/comic/
    # need to convert its format
    source = source.replace('href="//c.', 'href="https://c.')
    # some links are relative links
    # need to convert to absolute links
    source = source.replace('href="/', 'href="https://www.xkcd.com/')
    return source

def extract_links_from_single_webpage(web_url):
    """
    Given a website url as input, find all the webpage urls
    in the html of this website√
    """
    extracted_urls =[]
    source = read_html_webpage(web_url)
    count = source.count("<a href=")
    text = source
    for i in range(count):
        url, end = extract_link(text)
        # print(url.replace("\n",""))
        extracted_urls.append(url)
        text = text[end:]

    return extracted_urls

def main():
    webpage = "https://xkcd.com/"
    url = None
    urls = []

    urls = extract_links_from_single_webpage(webpage)
    print(urls)

if __name__ == "__main__":
    main()
