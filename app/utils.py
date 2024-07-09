from PIL import Image as PILImage

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def process_image(filepath):
    with PILImage.open(filepath) as img:
        img = img.resize((256, 256))
        img.save(filepath)
