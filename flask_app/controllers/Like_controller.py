from flask import Blueprint, redirect, session
from flask_app.model.Likes_model import Likes

likes_routes = Blueprint('likes', __name__)

class LikesController():
  @likes_routes.route('/like/<int:post_id>')
  def like(post_id):
    Likes().give_like(post_id, session.get('id'))
    return redirect('/thoughts')
  
  @likes_routes.route('/unlike/<int:post_id>')
  def unlike(post_id):
    Likes().give_dislike(post_id, session.get('id'))
    return redirect('/thoughts')