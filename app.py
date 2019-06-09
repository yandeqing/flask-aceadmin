from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
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


@app.route('/dropzone')
def dropzone():
    return render_template('dropzone.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/error-404')
def error_404():
    return render_template('error-404.html')


@app.route('/error-500')
def error_500():
    return render_template('error-500.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


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


@app.route('/nestable-list')
def nestable_list():
    return render_template('nestable-list.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/treeview')
def treeview():
    return render_template('treeview.html')


@app.route('/typography')
def typography():
    return render_template('typography.html')


@app.route('/widgets')
def widgets():
    return render_template('widgets.html')


@app.route('/wysiwyg')
def wysiwyg():
    return render_template('wysiwyg.html')
