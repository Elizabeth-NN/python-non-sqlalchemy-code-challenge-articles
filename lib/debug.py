from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine
def debug():
    print("=== Testing Author Class ===")
    # Test Author initialization and name property
    try:
        author1 = Author("John Doe")
        print(f"Author created: {author1.name}")  # Should print "John Doe"
    except Exception as e:
        print(f"Error creating author: {e}")

    # Test invalid author names
    try:
        author_invalid = Author("")  # Should raise ValueError
    except ValueError as e:
        print(f"Correctly caught empty name: {e}")

    try:
        author_invalid = Author(123)  # Should raise ValueError
    except ValueError as e:
        print(f"Correctly caught non-string name: {e}")

    print("\n=== Testing Magazine Class ===")
    # Test Magazine initialization and properties
    try:
        mag1 = Magazine("Tech Today", "Technology")
        print(f"Magazine created: {mag1.name}, {mag1.category}")  # Should print "Tech Today, Technology"
    except Exception as e:
        print(f"Error creating magazine: {e}")

    # Test invalid magazine names and categories
    try:
        mag_invalid = Magazine("A", "Tech")  # Should raise ValueError (name too short)
    except ValueError as e:
        print(f"Correctly caught short name: {e}")

    try:
        mag_invalid = Magazine("This Name Is Way Too Long For A Magazine", "Tech")  # Should raise ValueError
    except ValueError as e:
        print(f"Correctly caught long name: {e}")

    # Test property changes
    mag1.name = "New Tech Today"
    print(f"Changed name: {mag1.name}")  # Should print "New Tech Today"

    print("\n=== Testing Article Class ===")
    # Test Article creation
    try:
        article1 = Article(author1, mag1, "Python Programming Basics")
        print(f"Article created: {article1.title} by {article1.author.name} in {article1.magazine.name}")
    except Exception as e:
        print(f"Error creating article: {e}")

    # Test invalid article titles
    try:
        article_invalid = Article(author1, mag1, "Hi")  # Should raise ValueError (title too short)
    except ValueError as e:
        print(f"Correctly caught short title: {e}")

    # Test immutability of title
    try:
        article1.title = "New Title"  # Should raise AttributeError
    except AttributeError as e:
        print(f"Correctly prevented title change: {e}")

    print("\n=== Testing Relationships ===")
    # Add more articles for testing relationships
    article2 = Article(author1, mag1, "Advanced Python Techniques")
    mag2 = Magazine("Science Weekly", "Science")
    article3 = Article(author1, mag2, "The Science of Python")

    # Test author's articles
    print(f"{author1.name}'s articles:")
    for article in author1.articles():
        print(f"- {article.title}")

    # Test author's magazines
    print(f"\n{author1.name}'s magazines:")
    for magazine in author1.magazines():
        print(f"- {magazine.name}")

    # Test magazine's articles
    print(f"\n{mag1.name}'s articles:")
    for article in mag1.articles():
        print(f"- {article.title}")

    # Test magazine's contributors
    print(f"\n{mag1.name}'s contributors:")
    for author in mag1.contributors():
        print(f"- {author.name}")

    print("\n=== Testing Aggregate Methods ===")
    # Test author's topic areas
    print(f"{author1.name}'s topic areas: {author1.topic_areas()}")

    # Test magazine's article titles
    print(f"{mag1.name}'s article titles: {mag1.article_titles()}")

    # Add more articles to test contributing_authors
    Article(author1, mag1, "Python Design Patterns")
    Article(author1, mag1, "Python Performance Optimization")
    print(f"\n{mag1.name}'s contributing authors: {[a.name for a in mag1.contributing_authors()]}")

    # Test top_publisher
    print("\n=== Testing Top Publisher ===")
    print("Current top publisher:", Magazine.top_publisher().name if Magazine.top_publisher() else "None")

if __name__ == "__main__":
    debug()