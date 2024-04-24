from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import soundfile as sf

def crop_wav(input_file, output_file, start_time_sec, duration_sec):
    # Read the audio file
    audio, sample_rate = sf.read(input_file)

    # Convert time to samples
    start_sample = int(start_time_sec * sample_rate)
    end_sample = start_sample + int(duration_sec * sample_rate)

    # Crop the audio
    cropped_audio = audio[start_sample:end_sample]

    # Write the cropped audio to a new file
    sf.write(output_file, cropped_audio, sample_rate)

def convert_mp4_to_wav(input_file, output_file='output.wav'):
    # Load the video clip
    video_clip = VideoFileClip(input_file)
    
    # Extract audio from the video
    audio_clip = video_clip.audio
    # Convert audio to WAV format
    audio_clip.write_audiofile(output_file, codec='pcm_s16le', fps=audio_clip.fps)

    # Close the clips
    video_clip.close()
    audio_clip.close()

def on_progress(stream, chunk, bytes_remaining):
    print("Downloading...")

def on_complete(stream, file_path):
    print("Download Complete")