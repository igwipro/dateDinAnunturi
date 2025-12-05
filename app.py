from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "super_secret_123"

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

class User(UserMixin):
    id = 1
    username = "admin"
    password = "secret_12345"

@login_manager.user_loader
def load_user(user_id):
    return User()


playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=True)

def scrape_olx(url):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector("h4.css-hzlye5")
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    results = []

    listings = soup.select('div[type="list"].css-1apmciz')

    for card in listings:
        def get(selector):
            tag = card.select_one(selector)
            return tag.get_text(strip=True) if tag else None

        t_anunt = get("h4.css-hzlye5")
        t_pret = get("p.css-blr5zl")
        t_locatie = get("p.css-1b24pxk")

        t_suprafata = None
        surf_icon = card.find("svg", {"data-testid": "blueprint-card-param-icon"})
        if surf_icon:
            text_parts = list(surf_icon.parent.stripped_strings)
            if text_parts:
                t_suprafata = text_parts[-1]

        results.append({
            "t_anunt": t_anunt,
            "t_pret": t_pret,
            "t_locatie": t_locatie,
            "t_suprafata": t_suprafata
        })

    url_results = { 'url' : url , 'anunturi' : results}
    return url_results

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (request.form["username"] == User.username and
                request.form["password"] == User.password):
            login_user(User())
            return redirect(url_for("scrape_page"))
        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

@app.route("/scrape", methods=["GET", "POST"])
@login_required
def scrape_page():
    if request.method == "POST":
        url = request.form["url"]
        data = scrape_olx(url)
        return render_template("results.html", data=data)

    return render_template("scrape.html")

@app.route('/')
def hello():
    return "Demo for Bogdan!"
    
    
@app.teardown_appcontext
def shutdown_playwright(exception=None):
    #browser.close()
    #playwright.stop()
    print ('shutdown_playwright');
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8888, debug=True)
