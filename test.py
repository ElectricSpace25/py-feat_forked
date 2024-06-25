from feat import Detector

print("▶ Creating detector")
detector = Detector(device='cpu')
print("✓ Detector created")

video_path = "videos/friends_s01e01a_15sec.mp4"
skip_frames = 30
batch_size = 1

print("▶ Starting video detection")
video_prediction = detector.detect_video(video_path, skip_frames=skip_frames, batch_size=batch_size, memory_storage=True)
print("✓ Video detection complete")

print("▶ Saving to CSV")
video_prediction.to_csv('output.csv')
print("✓ CSV saved")