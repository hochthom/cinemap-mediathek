

import os
import glob
import shutil


def add_prefix(fn, country, prefix):
    c_old = '/%s' % country
    c_new = '/%s/%s' % (prefix, country)
    s_old = '/static'
    s_new = '/%s/static' % prefix
    
    tmp = []
    with open(fn, 'rb') as fp:
        for ln in fp.readlines():
            if len(ln.strip()) == 0:
                continue
            if '<a  href="/">Cinemap</a>' in ln:
                tmp.append(ln.replace('href="/">C', 'href="/'+prefix+'/">C'))
            elif s_old in ln:
                tmp.append(ln.replace(s_old, s_new))
            elif c_old in ln:
                tmp.append(ln.replace(c_old, c_new))
            else:
                tmp.append(ln)
        
    with open(fn, 'w') as fp:
        for line in tmp:
            fp.write(line)
            
def change_font(fn):
    tmp = []
    with open(fn, 'rb') as fp:
        for ln in fp.readlines():
            if len(ln.strip()) == 0:
                continue
            if 'href="http://fonts.go' in ln:
                tmp.append(ln.replace('href="http://fonts.go', 'href="https://fonts.go'))
            else:
                tmp.append(ln)
        
    with open(fn, 'w') as fp:
        for line in tmp:
            fp.write(line)
    
    

for path2 in glob.glob('D:/PROJ/GitHub/cinemap-mediathek/*'):
    if not os.path.isdir(path2):
        continue

    country = os.path.basename(path2)
    if country == 'static':
        continue
        
    print 'processing %s ...' % country
    for path, dirs, files in os.walk(path2):
        for f in files:
            if f.endswith('index.html'):
#                add_prefix(os.path.join(path, f), country, 'cinemap-mediathek')
                change_font(os.path.join(path, f))

#    dir_ = os.path.join(path2, 'orderby/popularity')
#    if not os.path.exists(dir_):
#        os.mkdir(dir_)
#        
#    fn = os.path.join(path2, 'orderby/popularity/index.html')
#    if not os.path.exists(fn):
#        fn = os.path.join(path2, 'index.html')
#        shutil.copy(fn, dir_)
    

  
  
        