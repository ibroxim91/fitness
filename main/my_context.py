from locals import lang_packages


def get_lange_packages(request):
    url = request.get_full_path()
    lang = url.split('/')[1]
    if  lang not in ("uz","ru","en"):
        lang  = "uz"
    return lang_packages[lang]  

