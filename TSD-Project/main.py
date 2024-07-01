import tkinter
from tkinter import *
import cv2
import numpy as np
import pyttsx3
from PIL import Image, ImageTk
import time
from customtkinter import *


class GUI:
    def __init__(self, root):
        self.app = root
        # getting screen width and height of display
        self.width = self.app.winfo_screenwidth()
        self.height = self.app.winfo_screenheight()
        # setting tkinter window size
        self.app.geometry("%dx%d" % (self.width, self.height))
        print("%d%d", self.width, self.height)
        # elf.app.state('zoomed')
        # app.attributes('-fullscreen', True)
        self.app.title("TSD")

        # Bind the app with Escape keyboard to
        # quit app whenever pressed
        self.app.bind('<Escape>', lambda e: self.app.quit())

        title = Label(self.app, text="TRAFFIC SIGN DETECTION SYSTEM", bd=10, relief=GROOVE,
                      font=("Times new roman", 40, "bold"),
                      bg="#9aecf9", fg="#030939")
        title.pack(side=TOP, fill=X)

        # ----------  Image1  Frame -----------

        Frame1 = Frame(self.app, bd=4, relief=RIDGE, bg="#030939")
        Frame1.place(x=40, y=100, width=580, height=800)

        # -------------for mandatory signs----------------------
        Image1 = LabelFrame(Frame1, text="Mandatory", bd=4, relief=RIDGE, bg="#9aecf9")
        Image1.place(x=10, y=30, width=553, height=275)

        arr = [33, 34, 35, 36, 37, 38, 39, 40]
        i = 0  # arr index
        for r in range(0, 2):
            for c in range(0, 4):
                s1 = "C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/signs/Mandatory/" + str(arr[i]) + ".png"
                image1 = Image.open(s1)
                resize_image1 = image1.resize((100, 100), Image.ANTIALIAS)
                new_pic1 = ImageTk.PhotoImage(resize_image1)
                label1 = tkinter.Label(Image1, image=new_pic1)
                label1.image = new_pic1
                label1.grid(row=r, column=c, padx=15, pady=10)
                i = i + 1

        # -------------for prohibitory signs----------------------
        Image2 = LabelFrame(Frame1, text="Prohibitory", bd=4, relief=RIDGE, bg="#9aecf9")
        Image2.place(x=10, y=340, width=553, height=415)

        arr = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16]
        i = 0  # arr index
        for r in range(0, 3):
            for c in range(0, 4):
                s1 = "C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/signs/Prohibitory/" + str(arr[i]) + ".png"
                image1 = Image.open(s1)
                resize_image1 = image1.resize((100, 100), Image.ANTIALIAS)
                new_pic1 = ImageTk.PhotoImage(resize_image1)
                label1 = tkinter.Label(Image2, image=new_pic1)
                label1.image = new_pic1
                label1.grid(row=r, column=c, padx=15, pady=10)
                i = i + 1

        # ----------  Manage Frame -----------

        ManageFrame = Frame(self.app, bd=4, relief=RIDGE, bg="#9aecf9")
        ManageFrame.place(x=675, y=100, width=573, height=800)

        # ManageFrame.grid_rowconfigure(0, weight=1)
        ManageFrame.grid_columnconfigure(0, weight=1)

        # Create a button to open the camera in GUI app

        dummy = Label(ManageFrame, font=("Times new roman", 25, "bold"), width=473, height=2, bg="#9aecf9",
                      fg="#030939")
        dummy.grid(row=0, columnspan=2, pady=20)

        camera_btn = CTkButton(ManageFrame, text="Open Camera", font=("Times new roman", 25, "bold"),
                               command=self.open_camera)
        camera_btn.grid(row=2, columnspan=2, pady=20)

        image_btn = CTkButton(ManageFrame, text="Select Image", font=("Times new roman", 25, "bold"),
                              command=self.open_image)
        image_btn.grid(row=4, columnspan=2, pady=20)

        video_btn = CTkButton(ManageFrame, text="Select Video", font=("Times new roman", 25, "bold"),
                              command=self.open_video)
        video_btn.grid(row=6, columnspan=2, pady=20)

        self.my_string_var = StringVar()
        l = Label(ManageFrame, textvariable=self.my_string_var, font=("Times new roman", 25, "bold"), width=473,
                  height=5, bg="#9aecf9", fg="#030939")
        l.grid(row=8, columnspan=2, pady=20)

        # ----------  Image Frame -----------

        Frame2 = Frame(self.app, bd=4, relief=RIDGE, bg="#030939")
        Frame2.place(x=1292, y=100, width=580, height=800)

        # -------------for other signs----------------------
        Image3 = LabelFrame(Frame2, text="Other", bd=4, relief=RIDGE, bg="#9aecf9")
        Image3.place(x=10, y=30, width=553, height=275)

        arr = [6, 12, 13, 14, 17, 32, 41, 42]
        i = 0  # arr index
        for r in range(0, 2):
            for c in range(0, 4):
                s1 = "C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/signs/other/" + str(arr[i]) + ".png"
                image1 = Image.open(s1)
                resize_image1 = image1.resize((100, 100), Image.ANTIALIAS)
                new_pic1 = ImageTk.PhotoImage(resize_image1)
                label1 = tkinter.Label(Image3, image=new_pic1)
                label1.image = new_pic1
                label1.grid(row=r, column=c, padx=15, pady=10)
                i = i + 1

        # -------------for danger signs----------------------
        Image4 = LabelFrame(Frame2, text="Danger", bd=4, relief=RIDGE, bg="#9aecf9")
        Image4.place(x=10, y=340, width=553, height=415)

        arr = [11, 18, 19, 20, 21, 23, 24, 26, 27, 28, 29, 31]
        i = 0  # arr index
        for r in range(0, 3):
            for c in range(0, 4):
                s1 = "C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/signs/Danger/" + str(arr[i]) + ".png"
                image1 = Image.open(s1)
                resize_image1 = image1.resize((100, 100), Image.ANTIALIAS)
                new_pic1 = ImageTk.PhotoImage(resize_image1)
                label1 = tkinter.Label(Image4, image=new_pic1)
                label1.image = new_pic1
                label1.grid(row=r, column=c, padx=15, pady=10)
                i = i + 1

    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def open_camera(self):
        # Define a video capture object
        camera = cv2.VideoCapture(0)

        # Declare the width and height in variables
        width, height = 800, 600

        # Set the width and height
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        # Capture the video frame by frame
        # _, frame = camera.read()

        h, w = 600, 800

        #loading yolov3 network
        with open('C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/ts/classes.names') as f:
            labels = [line.strip() for line in f]

        network = cv2.dnn.readNetFromDarknet('C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/darknet/build/darknet/x64/cfg/yolov3_ts_test.cfg',
                                             'C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/darknet/build/darknet/x64/weights/yolov3_ts.weights')

        layers_names_all = network.getLayerNames()

        layers_names_output = \
            [layers_names_all[i - 1] for i in network.getUnconnectedOutLayers()]

        probability_minimum = 0.5

        threshold = 0.3

        colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

        #reading frames in the loop
        while True:
            _, frame = camera.read()

            if w is None or h is None:
                h, w = frame.shape[:2]

            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                         swapRB=True, crop=False)


            network.setInput(blob)
            start = time.time()
            output_from_network = network.forward(layers_names_output)
            end = time.time()

            print('Current frame took {:.5f} seconds'.format(end - start))

            #getting bounding boxes
            bounding_boxes = []
            confidences = []
            class_numbers = []

            for result in output_from_network:
                for detected_objects in result:
                    scores = detected_objects[5:]
                    class_current = np.argmax(scores)
                    confidence_current = scores[class_current]

                    if confidence_current > probability_minimum:
                        box_current = detected_objects[0:4] * np.array([w, h, w, h])

                        x_center, y_center, box_width, box_height = box_current
                        x_min = int(x_center - (box_width / 2))
                        y_min = int(y_center - (box_height / 2))

                        bounding_boxes.append([x_min, y_min,
                                               int(box_width), int(box_height)])
                        confidences.append(float(confidence_current))
                        class_numbers.append(class_current)

            #start of non maximum suppression
            results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                                       probability_minimum, threshold)

            #drawing bounding boxes and labels
            if len(results) > 0:
                self.speak('Caution')
                for i in results.flatten():
                    x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
                    box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

                    colour_box_current = colours[class_numbers[i]].tolist()

                    cv2.rectangle(frame, (x_min, y_min),
                                  (x_min + box_width, y_min + box_height),
                                  colour_box_current, 2)

                    text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                           confidences[i])

                    cv2.putText(frame, text_box_current, (x_min, y_min - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, colour_box_current, 2)

                    self.speak(('{0} sign ahead !'.format(labels[int(class_numbers[i])])))
                    self.my_string_var.set(('Caution {0} sign ahead !'.format(labels[int(class_numbers[i])])))

            #showing processed frames
            cv2.namedWindow('Traffic Sign Detector', cv2.WINDOW_NORMAL)
            cv2.imshow('Traffic Sign Detector', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()

    def open_image(self):
        try:
            # Path of the image
            file_path = filedialog.askopenfilename()
            # Open file path
            uploaded = Image.open(file_path)
            uploaded.thumbnail(((self.ManageFrame.winfo_width() / 2.25), (self.ManageFrame.winfo_height() / 2.25)))
            im = ImageTk.PhotoImage(uploaded)
        except:
            pass
        image_BGR = cv2.imread(file_path)

        """cv2.namedWindow('OriginalImage', cv2.WINDOW_NORMAL)
        cv2.imshow('OriginalImage', image_BGR)
        cv2.waitKey(0)
        cv2.destroyWindow('OriginalImage')"""

        h, w = image_BGR.shape[:2]

        blob = cv2.dnn.blobFromImage(image_BGR, 1 / 255.0, (416, 416),
                                     swapRB=True, crop=False)
        with open('C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/ts/classes.names') as f:
            labels = [line.strip() for line in f]

        network = cv2.dnn.readNetFromDarknet('C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/darknet/build/darknet/x64/cfg/yolov3_ts_test.cfg',
                                             'C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/darknet/build/darknet/x64/weights/yolov3_ts.weights')

        layers_names_all = network.getLayerNames()

        layers_names_output = \
            [layers_names_all[i - 1] for i in network.getUnconnectedOutLayers()]

        probability_minimum = 0.5

        threshold = 0.3

        colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

        network.setInput(blob)
        start = time.time()
        output_from_network = network.forward(layers_names_output)
        end = time.time()

        print('Objects Detection took {:.5f} seconds'.format(end - start))

        bounding_boxes = []
        confidences = []
        class_numbers = []

        for result in output_from_network:
            for detected_objects in result:
                scores = detected_objects[5:]
                class_current = np.argmax(scores)
                confidence_current = scores[class_current]

                if confidence_current > probability_minimum:
                    box_current = detected_objects[0:4] * np.array([w, h, w, h])

                    x_center, y_center, box_width, box_height = box_current
                    x_min = int(x_center - (box_width / 2))
                    y_min = int(y_center - (box_height / 2))

                    bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                    confidences.append(float(confidence_current))
                    class_numbers.append(class_current)

        results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                                   probability_minimum, threshold)

        counter = 1

        if len(results) > 0:
            for i in results.flatten():
                print('Object {0}: {1}'.format(counter, labels[int(class_numbers[i])]))
                self.my_string_var.set('Caution! {0} sign ahead'.format(labels[int(class_numbers[i])]))
                self.speak('Caution! {0} sign ahead'.format(labels[int(class_numbers[i])]))

                counter += 1

                x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
                box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

                colour_box_current = colours[class_numbers[i]].tolist()

                cv2.rectangle(image_BGR, (x_min, y_min),
                              (x_min + box_width, y_min + box_height),
                              colour_box_current, 2)

                text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                       confidences[i])

                cv2.putText(image_BGR, text_box_current, (x_min, y_min - 5),
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, colour_box_current, 2)

        print()
        print('Total objects been detected:', len(bounding_boxes))
        print('Number of objects left after non-maximum suppression:', counter - 1)

        cv2.namedWindow('Detections', cv2.WINDOW_NORMAL)
        cv2.imshow('Detections', image_BGR)
        cv2.waitKey(0)
        cv2.destroyWindow('Detections')

    def open_video(self):
        try:
            # Path of the image
            file_path = filedialog.askopenfilename()
            print(file_path)
            """# Open file path
            uploaded = Image.open(file_path)
            uploaded.thumbnail(((self.ManageFrame.winfo_width() / 2.25), (self.ManageFrame.winfo_height() / 2.25)))
            im = ImageTk.PhotoImage(uploaded)"""
        except:
            pass

        video = cv2.VideoCapture(file_path+'')

        writer = None

        h, w = None, None

        with open('C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/ts/classes.names') as f:
            labels = [line.strip() for line in f]

        network = cv2.dnn.readNetFromDarknet(
            'C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/darknet/build/darknet/x64/cfg/yolov3_ts_test.cfg',
            'C:/Users/Preethi Yennemadi/Desktop/Final Year Project - TSD/TSD-data/darknet/build/darknet/x64/weights/yolov3_ts.weights')

        layers_names_all = network.getLayerNames()

        layers_names_output = \
            [layers_names_all[i - 1] for i in network.getUnconnectedOutLayers()]

        probability_minimum = 0.5

        threshold = 0.3

        colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

        f = 0

        t = 0

        while True:
            ret, frame = video.read()

            if not ret:
                break

            if w is None or h is None:
                h, w = frame.shape[:2]

            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                         swapRB=True, crop=False)

            network.setInput(blob)
            start = time.time()
            output_from_network = network.forward(layers_names_output)
            end = time.time()

            f += 1
            t += end - start

            print('Frame number {0} took {1:.5f} seconds'.format(f, end - start))

            bounding_boxes = []
            confidences = []
            class_numbers = []

            for result in output_from_network:
                for detected_objects in result:
                    scores = detected_objects[5:]
                    class_current = np.argmax(scores)
                    confidence_current = scores[class_current]

                    if confidence_current > probability_minimum:
                        box_current = detected_objects[0:4] * np.array([w, h, w, h])

                        x_center, y_center, box_width, box_height = box_current
                        x_min = int(x_center - (box_width / 2))
                        y_min = int(y_center - (box_height / 2))

                        bounding_boxes.append([x_min, y_min,
                                               int(box_width), int(box_height)])
                        confidences.append(float(confidence_current))
                        class_numbers.append(class_current)

            results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                                       probability_minimum, threshold)

            if len(results) > 0:
                for i in results.flatten():
                    x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
                    box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

                    colour_box_current = colours[class_numbers[i]].tolist()

                    cv2.rectangle(frame, (x_min, y_min),
                                  (x_min + box_width, y_min + box_height),
                                  colour_box_current, 2)

                    text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                           confidences[i])

                    cv2.putText(frame, text_box_current, (x_min, y_min - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, colour_box_current, 2)

                    if (f == 1):
                        self.my_string_var.set('Caution! {0} sign ahead'.format(labels[int(class_numbers[i])]))
                        self.speak('Caution! {0} sign ahead'.format(labels[int(class_numbers[i])]))

            if writer is None:
                # Constructing code of the codec
                # to be used in the function VideoWriter
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')

                writer = cv2.VideoWriter('D:/FinalYearProject/Traffic_sign/result-traffic.mp4', fourcc, 30,
                                         (frame.shape[1], frame.shape[0]), True)

            # Write processed current frame to the file
            writer.write(frame)

        # Printing final results
        print()
        print('Total number of frames', f)
        print('Total amount of time {:.5f} seconds'.format(t))
        print('FPS:', round((f / t), 1))

        # Releasing video reader and writer
        video.release()
        writer.release()


"""
# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()
"""

# Create a GUI app
root = CTk()
ob = GUI(root)
# Create an infinite loop for displaying app on screen
root.mainloop()
