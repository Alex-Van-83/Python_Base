from flask import (
    Blueprint,
    render_template,
    url_for,
)

about = Blueprint(
    "about",
    __name__,
)


@about.route("/about/")
def about_page():
    return render_template(
        "index.html",
        href_home=url_for('first.first_page'),
        name_home="Home",
        title='title from about',
        body='text from about',
    )
