import json
from util.Help import *
# DIEN 样本拆分
sql = '''
select seqs from tmp.last10hasorderuser_child_test where userid = 36861514
'''


def load_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line.split('<#>')

# 加载样本数据
a = list(load_csv('seq.csv'))

# 得到序列
print(len(a[0])) # a[0]表示一个用户,   a[0]的长度表示这个用户有几个大序列
b = a[0][0].strip().replace('[[','[').replace(']]',']').split('<%>') # 第一个大序列b

for user in a: # 多少个用户
    print('user: -------------- ')
    for bseq in user: # 多少个大序列
        print('bigseq: -------------- ')
        for sseq in bseq.strip().replace('[[','[').replace(']]',']').split('<%>'):
            print('smallseq: -------------- ')
            get_fields_data = list(map(lambda e:dict(zip(['acttime','actiontype'],[e['acttime'], e['actiontype']])),
                 json.loads(sseq)))[::-1]

            print(list(sample_seq(get_fields_data)))
