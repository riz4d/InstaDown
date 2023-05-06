import re
import os
from instaloader import Instaloader, Post
loader = Instaloader(download_videos=True, download_geotags=False, download_comments=False, compress_json=False)
def download_instagram_video(url):
    try:
       loader.load_session_from_file("instadownsession", filename="./instadownsession")
       match = re.search(r"(?:https?:\/\/)?(?:www\.)?(?:instagram\.com)\/(?:reel)\/([^\/?]+)", url)
       if not match:
           print("Invalid Instagram URL")
       shortcode = match.group(1)
       post = Post.from_shortcode(loader.context, shortcode)
       loader.download_post(post, target="ig_videos")
       media_file = None
       for file in os.listdir("ig_videos"):
           print(file)
           if file.endswith(".mp4"):
               media_file = "ig_videos/"+file
               break
       return media_file
    except Exception as e:
        print(e)
        return e
