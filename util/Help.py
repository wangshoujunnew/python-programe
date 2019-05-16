import time


def timediff(maxt, mint):
    """
    两个时间的秒数
    """
    times = list(map(lambda e: time.mktime(time.strptime(e[0:19], '%Y-%m-%d %H:%M:%S')), [maxt, mint]))
    return int(times[0] - times[1])


# timediff('2012-10-21 18:51:51', '2012-10-21 18:51:50')

def sample_seq(arr):
    """
    组成样本序列, 类型, 距离上一次行为的时间
    """
    for index, seq in enumerate(arr):
        lasttime_interval = None if index == 0 else timediff(seq['acttime'], arr[index - 1]['acttime'])  # 距离上一次行为的时间
        actiontype = seq['actiontype']  # 行为类型
        distance = seq['distance']  # 距离目的地的距离
        checkin_now = seq['checkin_now']  # 距离入住日期的间隔
        yield (lasttime_interval, actiontype, distance, checkin_now, seq['unitid'], seq['hotel_id'])


def datediff(maxt, mint):
    try:
        times = list(map(lambda e: time.mktime(time.strptime(e[0:10], '%Y-%m-%d')), [maxt, mint]))
        result = int(times[0] - times[1]) / (1 * 24 * 60 * 60)
    except:
        result = None
    return result


from math import radians, cos, sin, asin, sqrt


# python求两个经纬度的距离
def geodistance(destinationpos, userpos):
    """
    返回km,#lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    """
    try:
        lng1, lat1 = destinationpos.split(',')
        lng2, lat2 = userpos.split(',')

        lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
        dlon = lng2 - lng1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
        distance = round(distance / 1000, 3)
        return distance
    except:
        return None


def get_info(e):
    """
    需要返回的信息, 距离入住日期的距离, 距离目的地的距离
    """
    head = ['acttime', 'actiontype', 'checkin_now', 'distance', 'unitid', 'hotel_id']
    data = [
        e['acttime'], e['actiontype'], datediff(e['checkindate'], e['acttime']),
        geodistance(e['destinationpos'], e['userpos']), e['unitid'], e['hotel_id']
    ]
    return dict(zip(head, data))
