import os
import secrets
from PIL import Image
from flask import url_for, current_app


def save_picture(form_picture):
  # Random filename
  _, f_ext = os.path.splitext(form_picture.filename)
  new_name = secrets.token_hex(8) + f_ext
  image_path = os.path.join(current_app.root_path, 'static/profile_pics', new_name)
  print(f"new profile picture name: {new_name}")
  # Process Image
  output_size = (125, 125)
  i = Image.open(form_picture)
  i.thumbnail(output_size)
  i.save(image_path)
  return new_name
