import redis

class Cache_Emoji(object):
    def __init__(self,emoji,Db_Handler):
        self.emoji = emoji
        self.Handler = Db_Handler
    def Is_Exist(self):
        return self.Handler.exists(self.emoji) != 0
    def get_url(self):
        return self.Handler.hmget(self.emoji,'url')[0]
    def set_url(self,url):
        Payload = {'url': url}
        self.Handler.hmset(self.emoji,Payload)
    def get_next(self):
        return self.Handler.hmget(self.emoji,'next')[0]
    def get_prev(self):
        return self.Handler.hmget(self.emoji,'prev')[0]
    def set_next(self, next_emoji):
        Payload = {'next':next_emoji}
        self.Handler.hmset(self.emoji,Payload)
    def set_prev(self, prev_emoji):
        Payload = {'prev':prev_emoji}
        self.Handler.hmset(self.emoji,Payload)
    def name(self):
        return self.emoji


class Cache_DB(object):
    def __init__(self,size):
        self.Handler = redis.Redis(host='redis', port=6379)
        self.Head = 'None'
        self.Tail = 'None'
        self.size = size
        self.current_size = 0
        self.Handler.set('head',self.Head)
        self.Handler.set('tail',self.Tail)

    def set_head(self,new_head):
        self.Handler.set('head',new_head)
        self.Head = new_head

    def set_tail(self,new_tail):
        self.Handler.set('tail',new_tail)
        self.Tail = new_tail

    def get_emoji_url(self,emoji):
        emoji = Cache_Emoji(emoji,self.Handler)
        if emoji.Is_Exist():
            self.move_emoji_to_front(emoji)
            return emoji.get_url()
        else:
            return None

    def add_emoji(self,emoji,url):
        if self.current_size == self.size:
            self.remove_last_emoji()
            self.current_size -= 1
        emoji = Cache_Emoji(emoji,self.Handler)
        emoji.set_url(url)
        emoji.set_prev('None')
        if self.Head == 'None':
            self.set_head(emoji.name())
            self.set_tail(emoji.name())
            emoji.set_next('None')
        else:
            emoji_Head = Cache_Emoji(self.Head,self.Handler)
            emoji.set_next(emoji_Head.name())
            emoji_Head.set_prev(emoji.name())
            self.set_head(emoji.name())
        self.current_size += 1

    def move_emoji_to_front(self,emoji):
        if emoji.name() == self.Head:
            return
        elif emoji.name() == self.Tail:
            prev_emoji = Cache_Emoji(emoji.get_prev(),self.Handler)
            emoji_Head = Cache_Emoji(self.Head,self.Handler)
            prev_emoji.set_next('None')
            self.set_tail(prev_emoji.name())
            emoji.set_prev('None')
            emoji.set_next(emoji_Head.name())
            emoji_Head.set_prev(emoji.name())
            self.set_head(emoji.name())
        else:
            prev_emoji = Cache_Emoji(emoji.get_prev(),self.Handler)
            next_emoji = Cache_Emoji(emoji.get_next(),self.Handler)
            emoji_Head = Cache_Emoji(self.Head,self.Handler)
            prev_emoji.set_next(next_emoji.name())
            next_emoji.set_prev(prev_emoji.name())
            emoji.set_prev('None')
            emoji.set_next(emoji_Head.name())
            emoji_Head.set_prev(emoji.name())
            self.set_head(emoji.name())

    def remove_last_emoji(self):
        last_emoji = Cache_Emoji(self.Tail,self.Handler)
        self.set_tail(last_emoji.get_prev())
        self.Handler.delete(last_emoji.name())

    def destroy_db(self):
        self.Handler.flushdb()