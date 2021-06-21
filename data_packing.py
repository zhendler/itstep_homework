import json


class Book():
    
    def __init__(self, name, year, publisher, genre, author, price, review):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
        self.review = review
    
 
    def __str__(self):
        return f"About book:\nName: {self.name}\nGenre: {self.genre}\nAuthor: {self.author}\nPublisher: {self.publisher}\nYear: {self.year}\nPrice: {self.price}\nReview: {self.review}"
 
    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author
 
    def get_price(self):
        return self.price
        
        
 
B = Book(name="The Lord of the Rings: The Return of the King", year = "1955", publisher = "Allen & Unwin", genre = "High Fantasy, Adventure", author = "J. R. R. Tolkien", price = "PRICELESS", review = "No review")
book_dict = (B.__dict__)
# print(book_dict)

serialized = json.dumps(book_dict)
print(serialized)
desirialzied = json.loads(serialized)
print(desirialzied)


