from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = "AIzaSyC2NFe297Zsivvg1i3i_P5lcUCblQtmrkk"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(term, max_results):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=term,
    part="id,snippet",
    maxResults=max_results,
    type="video",
    videoDuration="medium",
    videoDefinition="high"
  ).execute()

  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("https://www.youtube.com/watch?v=%s" % search_result["id"]["videoId"])
  
  file = open("yt_links.txt","a") 
  
  file.write("\n".join(videos)+"\n")

if __name__ == "__main__":
  max_results = 50;
  bands = ['AC/DC','Guns N Roses','Queen','Bon Jovi','Metallica','Van Halen','Motley Crue',
                 'Aerosmith','Iron Maiden','Scorpions']
  try:
    for band in bands:
      youtube_search(band+' offical',max_results)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
