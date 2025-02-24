import cv2
import mediapipe as mp

# Inisialisasi modul MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Buka kamera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Konversi warna frame dari BGR ke RGB (diperlukan oleh MediaPipe)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Proses deteksi tangan
    results = hands.process(frame_rgb)
    
    # Jika terdeteksi tangan, gambar landmark
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Tampilkan hasil
    cv2.imshow("Hand Landmark Detection", frame)
    
    # Keluar dengan menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()