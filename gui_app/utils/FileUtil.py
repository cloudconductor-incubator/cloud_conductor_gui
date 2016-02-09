import re
from django.http import HttpResponse
import io
from django.conf import settings
from django.core.files import File
from django.http import *


# def download(request):
#
#     print("fileUtil now")
#     output = io.StringIO()
#     output.write("First line.\n")
#     response = HttpResponse(output.getvalue(), content_type="text/plain")
#     response["Content-Disposition"] = "filename=text.txt"
#     print("return now")
#
#     return response


def download_file(request):
    print("fileUtil now")
    response = HttpResponse(
        open('/path/to/downloadfile', 'rb').read(), mimetype='text/plain')
    response['Content-Disposition'] = 'filename=text.txt'
    return response
