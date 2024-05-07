from flask import Flask, render_template, request
import requests
import post, smtp

app = Flask(__name__)


#        Get API Data
# api = "https://api.npoint.io/c790b4d5cab58020d391"
api = "https://api.npoint.io/4b6c397d61266b54651d"
response = requests.get(api)
req = response.json()
posts = list()
for i in req:
    posts.append(post.Post(i['title'], i['subtitle'], i['id'], i['body'], i['image_url'], i['author']))
print(len(posts))


@app.route('/')
def home():
    return render_template("index.html", data=posts)

@app.route('/post/<num>')
def show_posts(num):
    print(posts)
    #data = dict(posts[int(num)])
    return render_template('post.html', data=posts, postid=int(num))


@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/contact')
def contact():

    return render_template('contact.html')


@app.route('/contact', methods=['POST'])
def receive_data():
    print(request.form['femail'])
    mail = smtp.SendContact(email=request.form['femail'], name=request.form['fname'], body=request.form['fbody'] )
    print(mail.body)
    mail.send_mail()
    return render_template('contacted.html')


if __name__ == "__main__":
    app.run(debug=True)