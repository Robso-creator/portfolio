import os
import subprocess
from datetime import datetime

import markdown2
from flask import Flask
from flask import render_template

app = Flask(__name__)

conteudo_pasta = os.listdir('posts')
conteudo_pasta.remove('placeholder.md')

posts_list = []
for post in conteudo_pasta:
    with open(f'posts/{post}', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    texto = markdown2.markdown(conteudo)
    paragrafos = texto.split('\n\n')

    dict_post = {
        'title': paragrafos[0].replace('<h1>', '').replace('</h1>', ''),
        'resume': ' '.join(texto.split('\n\n')[1].split()[:100]).replace('<p>', '').replace('</p>', ''),
        'post': post,
        'last_update': datetime.fromtimestamp(os.path.getmtime(f'posts/{post}')),
    }

    posts_list.append(dict_post)


@app.route('/')
def index():
    content_html = ''
    posts_list_ordened = sorted(
        posts_list, key=lambda x: x['last_update'], reverse=True,
    )

    # Pegar os quatro primeiros posts
    posts_list_ordened = posts_list_ordened[:4]
    for post in posts_list_ordened:
        string_template = """
        <a class="post" href="/posts/{POST}" target="_blank">
            <h4>{TITLE}</h4>
            <p>
                {RESUME}
            </p>
        </a>
        """
        resultado = string_template.format(
            TITLE=post['title'],
            RESUME=post['resume'],
            POST=post['post'].replace('.md', ''),
        )

        content_html += resultado

    return render_template('index.html', conteudo_html=content_html)


@app.route('/posts')
def blog():
    content_html = ''
    posts_list_ordened = sorted(
        posts_list, key=lambda x: x['last_update'], reverse=True,
    )

    # Pegar os quatro primeiros posts
    for post in posts_list_ordened:
        string_template = """
            <a class="post" href="/posts/{POST}" target="_blank">
                <h4>{TITLE}</h4>
                <p>
                    {RESUME}
                </p>
            </a>
            """
        resultado = string_template.format(
            TITLE=post['title'],
            RESUME=post['resume'],
            POST=post['post'].replace('.md', ''),
        )

        content_html += resultado

    return render_template('blog_posts.html', conteudo_html=content_html)


def get_file_last_modified(path):
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cd', '--date=unix', path],
            capture_output=True,
            text=True,
        )
        timestamp = int(result.stdout.strip())
        return datetime.fromtimestamp(timestamp)
    except:
        return datetime.now()

@app.route('/posts/<nome_pagina>')
def post_page(nome_pagina):
    path_post = os.path.join('posts', f'{nome_pagina}.md')
    if os.path.exists(path_post):
        tempo_modificacao = os.path.getmtime(path_post)
        data_modificacao = get_file_last_modified(path_post)

        with open(path_post) as arquivo_md:
            linhas = arquivo_md.readlines()

        indice_titulo = None
        for i, linha in enumerate(linhas):
            if linha.startswith('#'):
                indice_titulo = i
                break

        if indice_titulo is not None:
            linhas.insert(
                indice_titulo + 1,
                f"##### Last modified: {data_modificacao.strftime('%Y-%m-%d')}\n\n",
            )

        conteudo_md = ''.join(linhas)
        conteudo_html = markdown2.markdown(conteudo_md)

        return render_template('post.html', conteudo_html=conteudo_html)
    else:
        return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
