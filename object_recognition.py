import cv2
import supervision as sv
from ultralytics import YOLO


def main():
    # define resolution
    # cap = cv2.VideoCapture('rtsp://192.168.0.177:8080/h264_pcm.sdp')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    # Especifica o modelo YOLO a ser usado.
    model = YOLO("model/model_3dPrinted.pt")

    # Cria um dicionário de nomes de classes.
    class_names = {
        0: "espaguete",
        1: "amarrando",
        2: "espinhas",
    }

    # Cria um anotador de caixa delimitadora.
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    # Define a região de interesse.
    roi = (100, 100, 300, 300)

    # Inicie um loop para ler quadros do fluxo de vídeo.
    while True:
        ret, frame = cap.read()
        # Corta o quadro para a região de interesse.
        # frame = frame[roi[1]:roi[3], roi[0]:roi[2]]
        # Executa o modelo YOLO no quadro.
        result = model(frame, agnostic_nms=True)[0]
        # Extrai as detecções da saída YOLO.
        detections = sv.Detections.from_yolov8(result)
        # Obtem os rótulos para os objetos detectados.
        labels = [
            f"{class_names[detections.class_id[0]]} {detections.confidence[0]:.2f}"
            for _, confidence, class_id, a
            in detections.xyxy
        ]
        # Se algum objeto for detectado, imprime os rótulos e desenha as caixas delimitadoras no quadro.
        if len(detections.class_id) == 0:
            pass
        else:
            if detections.confidence[0] > 0.6:
                print(class_names[detections.class_id[0]])
                frame = box_annotator.annotate(
                    scene=frame,
                    detections=detections,
                    labels=labels
                )

        # Exibe o quadro.
        cv2.imshow("yolov8", frame)

        if cv2.waitKey(30) == 27:  # Quebra o loop quando a tecla ESC é pressionada.
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
