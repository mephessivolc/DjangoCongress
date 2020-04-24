import os
import uuid

from django.conf import settings
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        # ext = filename.split('.')[-1]
        ext = os.path.splitext(filename)[1]
        filename = "{}{}".format(uuid.uuid4(), ext)
        return os.path.join(self.sub_path, filename)
