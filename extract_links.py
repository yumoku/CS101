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
    if url != "" and url[0] == "\"":
        url = url[1:]
    return url, end

def read_html_webpage(web_url):
    """
    Read the contents of a webpage and modify
    the link url to absolute link url, also
    adjust the protocol-relative URL
    """
    session = requests.Session()
    session.max_redirects = 45
    source = session.get(web_url, verify=False).text
    # print(source)
    # some links are using protocol-relative URLs
    # such as //c.xkcd.com/random/comic/
    # need to convert its format
    source = source.replace('href="//c.', 'href="https://c.')
    # some links are relative links
    # need to convert to absolute links
    source = source.replace('href="/', f'href="{web_url}')
    return source

def clear_link_url_format(web_url):
    """
    Some urls are not HTTP or HTTPS url links,
    or some of them have the following format which need to be cleared
    <a href="http://www.asofterworld.com/archive.php">archives</a>...
    """
    formatted_web_url = ""
    index = 0
    if 'archive.php\'>archives' in web_url:
        index = web_url.find('archive.php\'>archives')
        formatted_web_url = web_url[:index + len('archive.php')]
    else:
        formatted_web_url = web_url

    return formatted_web_url

def extract_links_from_single_webpage(web_url):
    """
    Given a website url as input, find all the webpage urls
    in the html of this website√
    """
    url_formatted =""
    extracted_urls =[]
    source = read_html_webpage(web_url)
    count = source.count("<a href=")
    text = source
    for i in range(count):
        url, end = extract_link(text)
        # print(url.replace("\n",""))
        # The following if statement is working as a filter to filter url which don't
        # start with http, also filter some strange format url with more than 121
        # characters length
        if len(url) > 4 and url[0:4] == 'http' and len(url) < 121:
            url_formatted = clear_link_url_format(url)
            extracted_urls.append(url_formatted)
        text = text[end:]

    return extracted_urls

def main():
    webpage = "http://www.xkcd.com"
    url = None
    urls = []

    urls = extract_links_from_single_webpage(webpage)
    print(urls)

if __name__ == "__main__":
    main()
