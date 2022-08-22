from django.core.exceptions import ValidationError
from PIL import Image as Im
from django.core.files.images import get_image_dimensions

def validate_image_dimension(width, height):
    def check_fun(value):
        img_width, img_height = get_image_dimensions(value)
  
        if img_height != height or img_width != width:
            raise ValidationError(f'Image must be {width}px X {height}px')
    return check_fun

# def validate_image_dimension(value):
  
#   img_width, img_height = get_image_dimensions(value)
  
#   if img_height != 100 or img_width != 100:
#     raise ValidationError(f'Image must be 100px X 100px')

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_file_size(value):
    filesize= value.size
    print(filesize)
    if filesize > 85760:
        raise ValidationError("The maximum file size that can be uploaded is 200kb")
    else:
        return value
