def ExtractLinks(text: str):
    """
    This method is to find the beginning index
    and ending index of a web url
    :param text: target text to be searched
    :return: the indexes and new string removed the web url
    """
    target_string = "<a href=3D"
    target_sign = "\""
    anchor = text.find(target_string)
    begining = anchor + len('<a href=3D"')
    end = text.find(target_sign,begining + 1)
    url = text[begining:end]

    return url, end
def main():
    webpage = None
    url = None
    urls =[]
    try:
        with open("xkcd_ Good Science.mhtml","r") as file:
            webpage = file.read()
    except FileNotFoundError:
        print("Error, the html file was not found.")

    count = webpage.count("<a href=3D")
    text = webpage
    # print(f"count is {count}")

    for i in range(count):
        url, end = ExtractLinks(text)
        print(url.replace("\n",""))
        urls.append(url)
        text = text[end:]

if __name__ == "__main__":
    main()
