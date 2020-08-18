import time
from multiprocessing import Pool


def run(fn):
    # fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    print(fn * fn)


if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]

    pool = Pool(3)  # 创建拥有3个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    for fn in testFL:
        pool.apply_async(run, (fn,))
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print("并行执行")
