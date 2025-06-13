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

    return begining, end, text[end:]
def main():
    webpage = None
    url = None
    urls =[]
    index1 = 0
    index2 = 0
    ref = 0
    try:
        with open("xkcd_ Good Science.mhtml","r") as file:
            webpage = file.read()
    except FileNotFoundError:
        print("Error, the html file was not found.")

    count = webpage.count("<a href=3D")
    text = webpage
    print(f"count is {count}")

    for i in range(count):
        ref = index2
        index1, index2, text = ExtractLinks(text)
        index1 += ref
        index2 += ref
        urls.append((index1, index2))
        url = webpage[index1:index2]
        print(url.replace("\n",""))
    # the following parts are my trial-n-errors
    # in order to find the right answer
    # print(index1, index2)
    # print(webpage[index1:index2])
    # urls.append((index1, index2))
    # print(urls)
    # print(webpage[1777:1801])
    # print(webpage[(1801+34):(1801+59)])
    # print(webpage[(1801 + 59 + 104):(1801 + 59 + 129)])
    # for i in len(webpage):
    #     ExtractLinks(w)
if __name__ == "__main__":
    main()