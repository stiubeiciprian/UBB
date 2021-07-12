class Book {
  int id;
  String title;
  String author;
  String description;
  int numberOfPages;
  int currentPage;
  String genres;

  Book(
      {this.id,
      this.title,
      this.author,
      this.description,
      this.numberOfPages,
      this.currentPage,
      this.genres});

  factory Book.fromJson(Map<String, dynamic> json) {
    return Book(
      id: json['id'],
      title: json['title'],
      author: json['author'],
      description: json['description'],
      numberOfPages: json['number_of_pages'],
      currentPage: json['current_page'],
      genres: json['genres'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'author': author,
      'description': description,
      'number_of_pages': numberOfPages,
      'current_page': currentPage,
      'genres': genres,
    };
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'author': author,
      'description': description,
      'numberOfPages': numberOfPages,
      'currentPage': currentPage,
      'genres': genres,
    };
  }

  @override
  String toString() {
    return this.title;
  }
}
