from gestor.models import Article

def create_article(article):
  db_article = Article(**article)
  db_article.save()