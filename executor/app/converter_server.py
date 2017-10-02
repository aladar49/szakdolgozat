import youtube_dl
from os import remove, environ
from datetime import datetime
from ffmpy import FFmpeg
from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor

MAX_THREAD = int(environ['MAX_THREAD'])
app = Flask(__name__)

def convert(body):  
    timestamp = str('{:%Y%m%d_%H%M%S_%f}'.format(datetime.now()))
    ydl_opts = {
        'format': 'best[height<=1080]',
        'outtmpl': '/tmp/videos/'+timestamp
    }
    
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([body['yt_link']])   
    
    ff = FFmpeg(
        inputs={'/tmp/videos/'+timestamp: None},
        outputs={'/tmp/videos/'+timestamp+'.mp4': '-f mp4 -vf scale=320:-2 -c:a aac -strict -2'}
    )
    ff.run()
    remove('/tmp/videos/'+timestamp)
    
@app.route('/convert', methods=['POST'])
def converter_handle():
    runable_thread = MAX_THREAD
    for task in tasks:
        if not task.done():
            runable_thread -= 1
    if runable_thread > 0:
        body = request.json
        tasks.append(pool.submit(convert, body))
        return 'Proccess started', 200
    else:
        return 'There is not free thread.', 500

pool = ThreadPoolExecutor(max_workers = MAX_THREAD)
tasks = []

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
