import os
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level <= 1:
            print('{}:'.format(os.path.basename(root)))
        else:
            print('{}:'.format(os.path.basename(root)))
        for f in files:
          print('<div class=\"games\"><a href=\"download/resources/games/{}\">{}</a></div>'.format(f, f))

list_files(r'D:/Google Drive/Projects/Tableland Tutoring/resources/TpT Games')
