from html.parser import HTMLParser


class myHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = str()
        self.link_href = None
        self.link_text = None

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.result += "  \n"
        elif tag == "strong":
            self.result += "**"
        elif tag == "a":
            self.link_href = dict(attrs)['href']

    def handle_endtag(self, tag):
        if tag == "p":
            self.result += "\n\n"
        elif tag == "strong":
            self.result += "**"
        elif tag == "a":
            self.result += f"[{self.link_text}]({self.link_href})"
            self.link_text = None
            self.link_href = None

    def handle_data(self, data):
        if self.link_href is not None:
            self.link_text = self.link_text if self.link_text is not None else str()
            self.link_text += data
        else:
            self.result += data

    def get_result(self):
        self.close()
        return self.result


def markdownify(html: str):
    my_parser = myHTMLParser()

    html = [element.strip() for element in html.split()]
    html = ' '.join(html)
    my_parser.feed(html)
    html = my_parser.get_result()
    html = html.strip()
    return html
