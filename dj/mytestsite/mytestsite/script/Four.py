import cv2
import numpy as np
import imageio

def create_video(text):
	width, height = 112, 112
	fps = 30
	duration = 3

	# Создаем видео-файл
	name_of_file = text + '.mp4'
	video_writer = imageio.get_writer(name_of_file, fps=fps)

	# Количество кадров в видео
	num_frames = fps * duration

	for frame_num in range(num_frames):
		
		# Инициализируем OpenCV-изображение
		img = np.zeros((height, width, 3), dtype=np.uint8)
		img.fill(255)  #Фоновый цвет 0 - чёрный, 255 - белый, кодировка RGB256

		# Перерасчёт координат
		x = (width - len(text)) - (frame_num * len(text) / 4) * width / (fps * duration)
		y = height // 2
		#print(x, y)

		# Рисуем текст на изображении
		font = cv2.FONT_HERSHEY_DUPLEX # Устанавливаем шрифт
		font_scale = 1
		font_thickness = 1
		color = (0,0,0) # цвет текста
		cv2.putText(img, text, (int(x), y), font, font_scale, color, font_thickness, cv2.LINE_AA)

		# Добавляем текущий кадр в видео
		video_writer.append_data(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

	video_writer.close()
	return name_of_file

## Точка входа ##
if __name__ == "__main__":
	input_text = input("Введите текст для бегущей строки: ")
	t = create_video(input_text)
	print(t)
	print("Ваше видео готово!!")