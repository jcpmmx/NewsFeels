# NewsFeels
> Originally developed as a take-home test project for Muck Rack.

### System requirements
- Python (v3.6.5)
- PostgreSQL (v10.5)

### Built and tested with
- Python (v3.6.5)
- Django (v2.1.4)
- requests (v2.21)
- requests-html (v0.9.0)
- watson-developer-cloud (v2.5.1)
- python-dateutil (v2.7.5)
- PostgreSQL (v10.5) + psycopg2 (v2.7.6.1)
- gunicorn (v19.9) (Heroku only)
- django-heroku (v0.3.1) (Heroku only)

### How to run this locally
1. Clone this repo
2. Install all Python libraries (ideally inside a `virtualenv`): `pip install -r requirements.txt` 
3. Create 1 new PostgreSQL database: `createdb newsfeels`
4. Run `python manage.py migrate` to set your DB instance
5. Run `python manage.py runserver` to run Django's development server
6. Go to http://localhost:8000/articles/load and wait until initial data is populated
5. Now go to http://localhost:8000/articles to see the home page

---

### About this solution

This Django project is structured as follows:  

- One app, `articles`, that contains logic regarding the only model created so far: `Article`.  
  This model is for storing articles that have been analyzed already so we avoid doing so each time we go to the home page.
  It also contains the template for rendering the data table, as well as one custom template filter.

- A `nlp` package in charge of the NLP engine.  
This solution uses IBM's `Watson NLU` engine via their Python SDK.

- A `sources` package in charge of adding media outlets.  
This solution uses [News API](https://newsapi.org) so we don't bother on scraping manually each article source we want to add.  
Each implementation is a class that inherits from a base one with most of the logic for articles to be pulled and analyzed. The only required configurations are a `source` value (from News API) and the XPath to the contents of an article.  
CNN integration comes built-in.

- For simplicity, it uses Django's template system for the basic web pages we need to render.  
To make things prettier, `Bootstrap` and `jQuery` are used in the UI/UX side of things.

The idea is that every time we hit the home page, all articles that are already analyzed are loaded from DB and displayed.

The first time we see an article (we can tell that by checking that an `external ID` -made from bits of the article's data- is unique), we get its key information using News API and then visit the original source to download its contents.  
With a text version of the article, we then use Watson's NLU engine (via SDK) to get the sentiment analysis.  
Having the article's basic data and now its contents and sentiment, we create a new `Article` instance and save it to DB.

In the home page we display all available articles, sorted by most recent.  
Near the bottom of the table, we have a link that calls a small and secondary view that triggers the loading of new articles.  
If we detect there are new articles, the home page is refreshed via JS.

### Limitations
- News API and Watson's API limits due to free tiers

### Nice to haves
- Add more test cases
- Add a better separation between back-end and front-end by adding a full API and a separate client app (e.g. using React)
- Similar to above, improve the interaction with the async call to load articles by not forcing a page reload
- Make `nlp` work with classes that can be pluggable in case we want to cadd a new NLP engine (i.e. Google's)
- Automatically loop between available media outlets integrated so we go full plug-and-play
