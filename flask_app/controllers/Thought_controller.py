from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   session)

from flask_app.model.Thought_model import Thought
from flask_app.model.Likes_model import Likes
thoughts = Blueprint('thought', __name__)

class ThoughtController():

    @thoughts.route('/thoughts', methods=['GET'])
    def thought():
        posts_likeds = []  # Lista de posts likeados por el usuario actual
        likes = []
        posts = Thought().get_all_posts()
        for post in posts:
            likes_count = Likes().get_likes_from_post(post[0])
            likes.append(likes_count)
            # Obtén información sobre si el usuario actual dio like a este post
            user_liked = Likes().get_posts_liked_by_current_user(thought=post[0], user=session.get('id'))
            posts_likeds.append(user_liked)
        if session.get('logged_in'):
            return render_template('thoughts.html', name=session.get('name'), posts=Thought().get_all_posts(), likes=likes, current_user=session.get('id'), posts_likeds=posts_likeds)
        return redirect('/')
    

    @thoughts.route('/post', methods=['POST'])
    def post():
        content = request.form['content']
        owner = session.get('id')
        Thought().save_thought(content, owner)
        return redirect('/thoughts')

    @thoughts.route('/delete/<int:post_id>')
    def delete(post_id):
        result = Thought().delete_post(post_id, session.get('id'))
        print(result)
        return redirect('/thoughts')
