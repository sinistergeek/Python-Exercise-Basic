def path_filter(
        access_details_iter: Iterable[AccessDetails]
    ) -> Iterable[AccessDetails]:
    name_exclude = {
        'favicon.ico','robots.txt','index.php','humans.txt','dompdf.php','crossdomain.xml','_images','search.html','genindex.html','searchindex.js','modindex.html','py-modindex.html'
    }
    ext_exclude = {
        '.png','.js','.css'
    }
    for detail in access_details_iter:
        path = detail.url.path.split('/')
        if not any(path):
            continue
        if any(p in name_exclude for p in path):
            continue
        final = path[-1]
        if any(final.endswith(ext) for ext in ext_exclude):
            continue
        yield detail
