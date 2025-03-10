# 1 - Conectamos ao banco de dados
from sqlite3 import connect
conn = connect("db.sqlite3")
cursor = conn.cursor()

# 2 - Cramos a tablea caso não exista
conn.execute(
    """\
    CREATE TABLE if not exists post (
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """
)

# 3 - Criamos os post inicias para alimentar o banco de dados
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """\
        A linguem Python foi eleita a linguagem mais popular pela revista
        tech masters e segue dominando o mundo.
        """,
        "author": "Satoshi Namamoto",
    },
    {
        "title": "Como criar um blog utilizando Python",
        "content": """\
        Neste tutorial você aprenderá como criar um blog utilizando Python.
        <pre> import make_a_blog </pre>
        """,
        "author": "Guido Van Rossum",
    },
]

# 4 - Inserimos os post caso o banco de dados esteja vazio
count = cursor.execute("SELECT * FROM post;").fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author)
        """,
        posts,
    )
    conn.commit()

# 5 - Verificamos que foi realment inserido 
posts = cursor.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2
