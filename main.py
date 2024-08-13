import redis
r_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

def check_cache(func):
    def wrapper(n, *args, **kwargs):
        if r_cache.exists(n):
            res = r_cache.get(n)
            print(f'{n} is already cached: {res}')
            return int(res)
        res = func(n, *args, **kwargs)
        print(f'save into the cache {n} -> {res}')
        r_cache.set(n, res, ex=10)
        return res
    return wrapper

@check_cache
def fibo(n):
    if n <= 0:
        raise ValueError("Input n is zero")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    print(fibo(10))
