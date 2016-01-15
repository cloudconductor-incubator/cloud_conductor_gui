# -*- coding: utf-8 -*-
import csv
import io
from django.http import HttpResponse
from django.shortcuts import render
import sys
import json
from ..utils import ApiUtil
from ..utils.ApiUtil import Url


def testJsonForm(request):
#     def submitj(request):
    paramg = request.GET
    j = json.dumps(paramg)
    print(j)

    pm = json.loads(j)

    return HttpResponse(
        '''
        <html>
        <body>
        <h1>submit</h1>
        <form>
        A<input name="a" value="%s" ><br>
        B<input name="b" value="%s" ><br>
        C<input name="c" value="%s" ><br>
        <input type="submit"><br>

        %s
        </form>
        </body></html>
''' % (pm.get('a', ''), pm.get('b', ''), pm.get('c', ''), j))

#     return render(request, "gui_app/testFile/testJsonForm.html", {'file':'file upload complate' })


def testJsonForm2(request):
#     def submitj(request):
    paramg = request.GET
    j = json.dumps(paramg)
    print(j)

    pm = json.loads(j)
    url = Url.blueprintHistoriesParameters('1', '1', Url.url)
    data = {'auth_token': request.session['auth_token']}
    template = ApiUtil.requestGet(url, 'testJsonForm2', data)
    print(template)

    return render(request, "gui_app/testFile/testJsonForm.html", {'form':template })



def testUpload(request):

    print("testUpload")

    return render(request, "gui_app/testFile/testFileupload.html", {'file':'file upload complate' })

def testFileInput1(request):

    print("aaaa")

    return render(request, "gui_app/testFile/testFileupload3.html", {'file':'' })

def testFileInput3(request):

    print("test3")

    return render(request, "gui_app/testFile/testFileupload3.html", {'file':'' })

def testFileInput4(request):

    print("test4")

    return render(request, "gui_app/testFile/testFileupload4.html", {'file':'' })


def testFileInput5(request):

    print("test5")

    return render(request, "gui_app/testFile/testFileupload5.html", {'file':'' })


def testFileInput6(request):

    print("test6")

    return render(request, "gui_app/testFile/testFileupload6.html", {'file':'' })


def testFileInput7(request):

    print("test7")

    return render(request, "gui_app/testFile/testFileupload7.html", {'file':'' })


def testFileInput8(request):

    print("test8")

    return render(request, "gui_app/testFile/testFileupload8.html", {'file':'' })

def testFileInput9(request):

    print("test9")

    return render(request, "gui_app/testFile/testFileupload9.html", {'file':'' })


def testFileInput10(request):

    print("test10")

    return render(request, "gui_app/testFile/testFileupload10.html", {'file':'' })


def testFileInput11(request):
    print("test11")
    if request.method == "GET":

        return render(request, "gui_app/testFile/testFileupload11.html", {'file':'' })
    elif request.method == "POST":

        p = request.POST
        output = p.get('jsontext')

        d = download(request)
        download_file(request)
        download_2(request)
        some_view(request)
        print(d)

        return render(request, "gui_app/testFile/testFileupload11.html", {'file':'' })


def download(request):
    print('download now')

    output = io.StringIO()
    output.write('First line.\n')
    response = HttpResponse(output.getvalue(), content_type='text/plain')
    response["Content-Disposition"] = 'attachment; filename=C:\text\text.txt'
    print(2)
    return response

def download_file(request):
    print("download_file now")

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'filename=text.txt'
    return response

def download_2(request):
    print("download_2 now")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=foo.csv'
    writer = csv.writer(response)
    writer.writerow(['スパム', 'エッグ', 'ベーコン'])
    writer.writerow(['spam', 'egg', 'bacon'])
    return response

def some_view(request):
    print("some_view now")
    # 適切な CSV 用ヘッダとともに HttpResponse オブジェクトを生成します。
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=somefilename.csv'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

def download_3():

    url = sys.argv[1]
    title = sys.argv[2]
    urllib.urlretrieve(url,"{0}".format(title))

if __name__ == "__main__":
    download()
