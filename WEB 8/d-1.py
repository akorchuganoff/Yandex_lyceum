from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/galery', methods=['GET', "POST"])
def carousel():
    global images
    if request.method == "GET":
        return render_template('carousel.html', images=images)
    elif request.method == 'POST':
        print(request.files)
        img = request.files['file']
        fname = img.filename
        img.save(f"static/img/{fname}")
        images.append(f"static/img/{fname}")
        return redirect('/galery')



if __name__ == '__main__':
    images = ['static/img/2.jpg', 'static/img/3.jpeg']
    app.run(host='localhost', port=8080, debug=True)
