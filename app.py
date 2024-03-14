from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blog():
    return render_template('index.html', page='blog')

@app.route('/projects')
def projects():
    return render_template('projects.html', page='projects')

@app.route('/cv')
def cv():
    return render_template('cv.html', page='cv')


@app.route('/photos')
def photos():
    photos = [
        {'filename': 'photo1.jpeg', 'alt': 'Photo 1'},
        {'filename': 'photo2.jpeg', 'alt': 'Photo 2'},
        {'filename': 'photo3.jpeg', 'alt': 'Photo 3'},
        # Add more photo data as needed
    ]
    return render_template('photos.html', page='photos', photos=photos)


if __name__ == '__main__':
    app.run(debug=True)
