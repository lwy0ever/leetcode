from urllib.parse import urlparse,urlunparse

class Codec:
    def __init__(self):
        self.d = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        parse_res = urlparse(longUrl)
        u = parse_res[2] + parse_res[4]
        shortUrl = '/' + str(abs(hash(u)))
        self.d[shortUrl] = longUrl
        #print(shortUrl)
        return urlunparse(('http','tinyurl.com',shortUrl,'','',''))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        #print(shortUrl)
        parse_res = urlparse(shortUrl)
        return self.d[parse_res[2] + parse_res[4]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))