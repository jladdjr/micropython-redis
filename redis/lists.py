from .client import Client


class RedisLists(Client):
    def blpop(self, *args):
        return self.execute_command('BLPOP', *args)

    def brpop(self, *args):
        return self.execute_command('BRPOP', *args)

    def brpoplpush(self, *args):
        return self.execute_command('BRPOPLPUSH', *args)

    def lindex(self, *args):
        return self.execute_command('LINDEX', *args)

    def linsert(self, *args):
        return self.execute_command('LINSERT', *args)

    def llen(self, *args):
        return self.execute_command('LLEN', *args)

    def lpop(self, *args):
        return self.execute_command('LPOP', *args)

    def lpush(self, *args):
        return self.execute_command('LPUSH', *args)

    def lpushx(self, *args):
        return self.execute_command('LPUSHX', *args)

    def lrange(self, *args):
        return self.execute_command('LRANGE', *args)

    def lrem(self, *args):
        return self.execute_command('LREM', *args)

    def lset(self, *args):
        return self.execute_command('LSET', *args)

    def ltrim(self, *args):
        return self.execute_command('LTRIM', *args)

    def rpop(self, *args):
        return self.execute_command('RPOP', *args)

    def rpoplpush(self, *args):
        return self.execute_command('RPOPLPUSH', *args)

    def rpush(self, *args):
        return self.execute_command('RPUSH', *args)

    def rpushx(self, *args):
        return self.execute_command('RPUSHX', *args)
