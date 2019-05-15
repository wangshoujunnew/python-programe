import time

def timediff(maxt, mint):
    """
    时间之间的描述
    :return: 秒数
    """
    times = list(map(lambda e: time.mktime(time.strptime(e[0:19], '%Y-%m-%d %H:%M:%S')), [maxt, mint]))
    return int(times[0] - times[1])

def sample_seq(arr):
    """
    组成样本序列, 类型, 距离上一次行为的时间
    """
    for index,seq in enumerate(arr):
        yield (None if index == 0 else timediff(seq['acttime'], arr[index-1]['acttime']), seq['actiontype'])

if __name__ == '__main__':
    print(timediff("2019-04-22 19:25:20", "2019-04-22 19:25:18"))
