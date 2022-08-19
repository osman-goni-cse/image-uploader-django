from django.core.exceptions import ValidationError
from PIL import Image as Im
from django.core.files.images import get_image_dimensions

def validate_image_dimension(value):
  
  img_width, img_height = get_image_dimensions(value)
  
  if img_height != 300 or img_width != 300:
    raise ValidationError('Image must be 300px X 300px')

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
