from flask import (
    Blueprint,
    render_template,
    url_for,
)

main = Blueprint(
    "first",
    __name__,
)


@main.route("/")
def first_page():
    return render_template(
        "index.html",
        href_home=url_for('about.about_page'),
        name_home="About",
        title='title from main',
        body='text from main',
    )
