import pandas as pd
import requests
from time import sleep

# Facebook API ke liye credentials aur parameters
access_token = 'EAAOAouTfDpsBO1DpZAHFvsn9TTZBsAJni12JU9ZBY0Xq1Ql6kQCq5xOCQ2UZCuERPlnhkecqycXE62xGVOmG17hPUjRWyyoTw26FEwBbdvhho0PISspBovLKh5O9tuFq5RsqdLxl4UszCEL3ZAuFZCTBZCbwMMUqE1CPJnuXJtEQlUZBwfJetkzfxez9k2exkpIZD'
page_id = '247607515094289'

def upload_video_to_facebook(video_url, description):
    # Video file download karein
    response = requests.get(video_url)
    video_file_path = '/tmp/video.mp4'
    with open(video_file_path, 'wb') as file:
        file.write(response.content)

    # Facebook API URL for video upload
    upload_url = f'https://graph.facebook.com/v20.0/{page_id}/videos'

    # Facebook pe video upload karein
    with open(video_file_path, 'rb') as video_file:
        upload_response = requests.post(upload_url, files={'file': video_file}, data={
            'access_token': access_token,
            'description': description
        })

    # Response check karein
    if upload_response.status_code == 200:
        print(f'Video uploaded successfully from URL: {video_url}')
    else:
        print(f'Error uploading video from URL {video_url}: {upload_response.text}')

def process_csv_and_upload(csv_file_path):
    df = pd.read_csv(csv_file_path)
    for _, row in df.iterrows():
        video_url = row['video_url']
        description = row['description'] if 'description' in row else 'Default description'
        upload_video_to_facebook(video_url, description)
        sleep(600)  # Agla video upload karne se pehle 10 minutes wait karein

if __name__ == "__main__":
    import sys
    csv_file_path = 'path/to/your/csv_file.csv'  # Repository me CSV file ka path
    process_csv_and_upload(csv_file_path)
