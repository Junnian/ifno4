这个版本是为了把某个作者的合著作者信息也加入爬取队列

scholar.py   是爬关键词直接关联的作者，并将这些作者的合著作者直接保存再copurl.txt文件里     作者信息结果保存在如表名为‘aerospace’这样的表里

copinfo.py   是从copurl.txt文件里读取url,并爬取这些信息 ，并将这些作者的合著直接保存再copurl1.txt文件里                                 作者信息结果保存在如表名为‘aerospace_c'这样的表里

copinfo2.py   是从copurl.txt文件里读取url,并爬取这些信息 ，并将这些作者的合著直接保存再copurl2.txt文件里 


copinfo3.py   是从copur2.txt文件里读取url,并爬取这些信息 ，并将这些作者的合著直接保存再copurl3.txt文件里 


otherauthor.py  爬取逻辑是，以key或new里的文件为初始关键词，每爬到一个作者，就将这个作者的所属领域添加到待爬id中,将爬到的领域写到field.txt中