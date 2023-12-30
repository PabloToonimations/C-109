import cv2
import math
import mediapipe as mp
from pynput.mouse import Button, Controller
import pyautogui

mouse=Controller()

cap = cv2.VideoCapture(0)

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

(screen_width, screen_height) = pyautogui.size()

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

pinch=False

# Definir una función para contar dedos
def countFingers(image, hand_landmarks, handNo=0):

    global pinch
    
    if hand_landmarks:
        # Obtener todas las marcas de referencia en la primera mano visible
        landmarks = hand_landmarks[handNo].landmark

        # Contar dedos
        fingers = []

        for lm_index in tipIds:
            # Obtener los valores de la poscición "y" de la punta y parte inferior del dedo
            finger_tip_y = landmarks[lm_index].y
            finger_bottom_y = landmarks[lm_index - 2].finger_tip_y

            # Verificar si algun dedo esta abiero o cerrado
            if lm_index !=4:
                if finger_tip_y < finger_bottom_y:
                    fingers.append(1)