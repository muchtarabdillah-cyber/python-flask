from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

nama_blog = "Mini Blog"

daftar_post = [
    {
        "id": 1,
        "judul": "Belajar Flask",
        "penulis": "Admin",
        "isi": "Flask adalah micro-framework Python."
    },
    {
        "id": 2,
        "judul": "Belajar Jinja2",
        "penulis": "Admin",
        "isi": "Jinja2 adalah mesin template untuk Flask."
    },
    {
        "id": 3,
        "judul": "Belajar Routing",
        "penulis": "Budi",
        "isi": "Routing menghubungkan URL dengan fungsi Python."
    }
]


@app.route("/")
def home():
    return render_template(
        "latihan.html",
        nama_blog=nama_blog,
        posts=daftar_post
    )


@app.route("/about")
def about():
    return render_template(
        "latihan.html",
        nama_blog=nama_blog,
        halaman="about"
    )


@app.route("/posts")
def posts():
    return render_template(
        "latihan.html",
        nama_blog=nama_blog,
        posts=daftar_post,
        halaman="posts"
    )


@app.route("/post/<int:id>")
def post_detail(id):
    for post in daftar_post:
        if post["id"] == id:
            return render_template(
                "latihan.html",
                nama_blog=nama_blog,
                post=post,
                halaman="detail"
            )

    return "Artikel tidak ditemukan", 404


if __name__ == "__main__":
    app.run(debug=True, port=8080)