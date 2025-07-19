from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)

@app.route('/transcript', methods=['POST'])
def get_transcript():
    data = request.json
    video_id = data.get('video_id')
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = ' '.join([item['text'] for item in transcript])
        return jsonify({'transcript': full_text})
    except Exception as e:
        return jsonify({'error': str(e), 'transcript': ''}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
