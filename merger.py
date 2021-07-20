import moviepy.editor as mpe

clip = mpe.VideoFileClip("Recordedf.mp4")
audio_bg = mpe.AudioFileClip("voice.mp3")
final_audio = mpe.CompositeAudioClip([audio_bg, clip.audio])
final_clip = clip.set_audio(final_audio)
final_clip.write_videofile("output.mp4")
