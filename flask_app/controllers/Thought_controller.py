from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   session)

from flask_app.model.Thought_model import Thought
from flask_app.model.Likes_model import Likes
thoughts = Blueprint('thought', __name__)

class ThoughtController():

    @thoughts.route('/thoughts', methods=['GET'])
    def thought():
        likes = []
        posts = Thought().get_all_posts()
        for post in posts:
            likes_count = Likes().get_likes_from_post(post[0])
            likes.append(likes_count)
        if session.get('logged_in'):
            return render_template('thoughts.html', name=session.get('name'), posts=Thought().get_all_posts(), likes=likes)
        return redirect('/')

    @thoughts.route('/post', methods=['POST'])
    def post():
        content = request.form['content']
        owner = session.get('id')
        result = Thought().save_thought(content, owner)
        if result == "Publicación guardada":
            flash('Melos')
        else:
            flash('Error al publicar')
        return redirect('/thoughts')

    @thoughts.route('/delete/<int:post_id>')
    def delete(post_id):
        result = Thought().delete_post(post_id, session.get('id'))
        print(result)
        return redirect('/thoughts')
