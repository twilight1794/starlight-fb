from fbchat import models
from rules import *

@regex(r'(@(Starlight|(Anne)? Frye) )?(chinga.*|p[uv]ta|fu[ck]* ?of+|ya c[aá]llate|ctm)( @(Starlight|(Anne)? Frye))?')
def run(**kwargs):
    kwargs['fbobj'].sendRemoteFiles('https://i.blogs.es/f64f57/650_1000_nvidia-fuckyou/1366_2000.jpg', message=Message('._.', reply_to_id=kwargs['message_object'].uid), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
