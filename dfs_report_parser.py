import re

import pandas as pd

file = open('d:/test/dfstest/dfs_report_20210831.txt')
flist = []
fsub = []
flist = re.split('\n\n', file.read())
for content in flist:
    if content and (content.startswith('Name') or 'Name' in content):
        fsub.append(re.sub(r'\n\n|^\n', '', content))

slist = []
for d in fsub:
    dic = dict({i.split(': ')[0]: i.split(': ')[1] for i in d.split('\n')})
    slist.append(dic)
ff = pd.DataFrame(slist)
print(ff)
ff.to_csv('dfs_report_20210831.csv', index=True, header=True)
