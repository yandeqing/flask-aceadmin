from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


@app.route('/blank')
def blank():
    return render_template('blank.html')


@app.route('/buttons')
def buttons():
    return render_template('buttons.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/content-slider')
def content_slider():
    return render_template('content-slider.html')


@app.route('/dropzone')
def dropzone():
    return render_template('dropzone.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/email-confirmation')
def email_confirmation():
    return render_template('email-confirmation.html')


@app.route('/email-contrast')
def email_contrast():
    return render_template('email-contrast.html')


@app.route('/email-navbar')
def email_navbar():
    return render_template('email-navbar.html')


@app.route('/email-newsletter')
def email_newsletter():
    return render_template('email-newsletter.html')


@app.route('/email')
def email():
    return render_template('email.html')


@app.route('/error-404')
def error_404():
    return render_template('error-404.html')


@app.route('/error-500')
def error_500():
    return render_template('error-500.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/form-elements-2')
def form_elements_2():
    return render_template('form-elements-2.html')


@app.route('/form-elements')
def form_elements():
    return render_template('form-elements.html')


@app.route('/form-wizard')
def form_wizard():
    return render_template('form-wizard.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/grid')
def grid():
    return render_template('grid.html')


@app.route('/inbox')
def inbox():
    return render_template('inbox.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/invoice')
def invoice():
    return render_template('invoice.html')


@app.route('/jqgrid')
def jqgrid():
    return render_template('jqgrid.html')


@app.route('/jquery-ui')
def jquery_ui():
    return render_template('jquery-ui.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/mobile-menu-1')
def mobile_menu_1():
    return render_template('mobile-menu-1.html')


@app.route('/mobile-menu-2')
def mobile_menu_2():
    return render_template('mobile-menu-2.html')


@app.route('/mobile-menu-3')
def mobile_menu_3():
    return render_template('mobile-menu-3.html')


@app.route('/nestable-list')
def nestable_list():
    return render_template('nestable-list.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/top-menu')
def top_menu():
    return render_template('top-menu.html')


@app.route('/treeview')
def treeview():
    return render_template('treeview.html')


@app.route('/two-menu-1')
def two_menu_1():
    return render_template('two-menu-1.html')


@app.route('/two-menu-2')
def two_menu_2():
    return render_template('two-menu-2.html')


@app.route('/typography')
def typography():
    return render_template('typography.html')


@app.route('/widgets')
def widgets():
    return render_template('widgets.html')


@app.route('/wysiwyg')
def wysiwyg():
    return render_template('wysiwyg.html')
