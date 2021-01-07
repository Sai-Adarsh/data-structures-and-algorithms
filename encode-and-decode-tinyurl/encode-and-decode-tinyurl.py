class Codec:
​
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        from random import randint
        self.hash_table = {}
        self.to_be_assinged = randint(10000, 99999)
        self.hash_table[str(self.to_be_assinged)] = longUrl
        return "http://tinyurl.com/" + str(self.to_be_assinged)
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split('/')[-1]
        return self.hash_table[shortUrl]
        
​
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
