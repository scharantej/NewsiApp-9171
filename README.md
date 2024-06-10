## Flask Application Design for Recent Newspaper Articles Website

**HTML Files**

- **index.html:**
   - Front page of the website.
   - Displays a list of recent newspaper articles.
   - Each article includes a headline, a snippet, and a link to the full article.
- **article.html:**
   - Displays the complete content of a specific article.
   - Includes the article's headline, author, publication date, and body text.

**Routes**

- **@app.route('/')**
   - **GET:** Renders the `index.html` file and passes the list of recent articles to the template.
   - **POST:** Not implemented.
- **@app.route('/article/<article_id>')**
   - **GET:** Renders the `article.html` file and passes the specified article data to the template.
   - **POST:** Not implemented.