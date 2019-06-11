#!/usr/bin/env python
# coding=utf-8
'''
@author: Zuber
@date:  2019/6/5 10:04
'''
import os
import re


def get_full_dir(path, *paths):
    currentFile = os.getcwd()
    proDir = currentFile[:currentFile.find("flask-aceadmin")] + "flask-aceadmin"
    return os.path.join(proDir, path, *paths)


def get_lastmodify_file(test_report):
    if os.path.isdir(test_report):
        lists = os.listdir(test_report)
        lists.sort(key=lambda fn: os.path.getmtime(test_report + os.path.sep + fn))
        if len(lists) > 0:
            return get_lastmodify_file(os.path.join(test_report, lists[-1]))
        else:
            return test_report
    else:
        return test_report


def del_file(path):
    try:
        if os.path.isfile(path):
            if os.path.exists(path):
                os.remove(path)
        else:
            ls = os.listdir(path)
            for i in ls:
                c_path = os.path.join(path, i)
                del_file(c_path)
    except:
        pass


def getstringfromfile(filepath):
    content = None
    try:
        file = open(filepath, "r", encoding='utf-8')
        content = file.read()
        file.close()
    except Exception as e:
        print(f"{e}")
    return content


def replace_templetstr_tofile(filepath, content):
    '''
    替换html中的公共模块为
    {% extends "admin-base.html" %}
    {% block body %}
    <body></body>
    {% endblock %}
    :param filepath:
    :return:
    '''
    import codecs
    file = codecs.open(filepath, 'w', 'utf-8')
    html = '{% extends "admin-base.html" %}' \
           '{% block body %}' \
           + content \
           + '{% endblock %}'
    print(f"【replace_templetstr_tofile().html={html}】")
    return write_to_file(filepath, html)


def write_to_file(filepath, content):
    '''
    :return:
    '''
    try:
        import codecs
        file = codecs.open(filepath, 'w', 'utf-8')
        file.write(content)
        file.close()
    except Exception as e:
        print(f"{e}")
        return False
    return True


def add_route(filepath, route_name):
    '''
    替换html中的公共模块为
    @app.route('/route_name')
    def route_name():
        return render_template('route_name.html')
    :param filepath:
    :return:
    '''
    try:
        import codecs
        file = codecs.open(filepath, 'a', 'utf-8')
        name = route_name.replace("-", "_")
        html = f"@app.route('/{route_name}')\ndef {name}():\n    return render_template('{route_name}.html')\n\n\n"
        file.write(html)
        file.close()
    except Exception as e:
        print(f"{e}")
        return False
    return True


def search_files(dir):
    files = []
    lists = os.listdir(dir)
    for file in lists:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            entity = {}
            entity['path'] = path
            entity['filename'] = file
            files.append(entity)
    return files


def extrahtml_by_tag(html, tag):
    from bs4 import BeautifulSoup  # 导入库
    # 假设html是需要被解析的html
    # 将html传入BeautifulSoup 的构造方法,得到一个文档的对象
    soup = BeautifulSoup(html, 'html.parser')
    # 查找所有的h4标签
    links = soup.find(tag)
    return links


def batch_repalce_templet_str():
    full_dir = get_full_dir('templates')
    files = search_files(full_dir)
    for file in files:
        if '.html' in file['filename']:
            stringfromfile = getstringfromfile(file['path'])
            if "url_for" in stringfromfile:
                print(f"【files={file}】")
                body = extrahtml_by_tag(stringfromfile, "body")
                # replace_templetstr_tofile(file['path'],
                #                           str(body).replace("<body>", '').replace('</body>', ''))
                add_route(get_full_dir('app.py'),
                          file['filename'].replace('.html', ''))

htmlreplaces = []
jsreplaces = []
cssreplaces = []

def replace_style_script(htmlstr):
    replaces = []
    data = re.findall(r'href="(\S+)"', htmlstr)
    if data:
        replaces.extend(data)
    data = re.findall(r'src="(\S+)"', htmlstr)
    if data:
        replaces.extend(data)
    list = set(replaces)
    for item in list:
        if item and "https://" not in item and "http://" not in item and "#" not in item:
            if ".html" in item:
                htmlstr = htmlstr.replace(item, item.replace('.html', ''))
                htmlreplaces.append(item)
            elif "url_for" not in item:
                filename_s_item = r"{{ url_for('static', filename='%s') }}" % item
                htmlstr = htmlstr.replace(item, filename_s_item)
                if ".js" in item:
                    jsreplaces.append(item)
                if ".css" in item:
                    cssreplaces.append(item)
    replaces.clear()
    data = re.findall(r"href='(\S+)'", htmlstr)
    if data:
        replaces.extend(data)
    data = re.findall(r"src='(\S+)'", htmlstr)
    if data:
        replaces.extend(data)
    list = set(replaces)
    for item in list:
        if item and "https://" not in item and "http://" not in item and "#" not in item:
            if ".html" in item:
                htmlstr = htmlstr.replace(item, item.replace('.html', ''))
                htmlreplaces.append(item)
            elif "url_for" not in item:
                s_item = r'{{ url_for("static", filename="%s") }}' % item
                htmlstr = htmlstr.replace(item, s_item)
                if ".js" in item:
                    jsreplaces.append(item)
                if ".css" in item:
                    cssreplaces.append(item)
    return htmlstr


def batch_replace_style_script():
    full_dir = get_full_dir('templates')
    files = search_files(full_dir)
    for file in files:
        if '.html' in file['filename']:
            stringfromfile = getstringfromfile(file['path'])
            if stringfromfile:
                tag = extrahtml_by_tag(stringfromfile, "html")
                data = replace_style_script(str(tag))
                write_to_file(file['path'], data)


def batch_add_routes():
    full_dir = get_full_dir('templates')
    files = search_files(full_dir)
    for file in files:
        if '.html' in file['filename']:
            add_route(get_full_dir('app.py'),
                      file['filename'].replace('.html', ''))


def print_arr(arr):
    for item in arr:
        print(item)


if __name__ == '__main__':
    # batch_replace_style_script()
    # print_arr(htmlreplaces)
    # print_arr(jsreplaces)
    # print_arr(cssreplaces)
    batch_add_routes()
