import cv2
import time
import mediapipe as mp


cap=cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#mediapipe kütüphanesinden hands objelerini çagır
mpHand=mp.solutions.hands

#hands fonksiyonu
hands=mpHand.Hands()

#hads çizdirmek için mp kütüphanesinin drawing_util kullanılır.
mpDraw=mp.solutions.drawing_utils

pTime=0
cTime=0

#Video kaydedici fourcc çerçeveleri kaydetmek için codec kodu
writer=cv2.VideoWriter("hands_video.mp4",cv2.VideoWriter_fourcc(*"DIVX"),
                       20,(width,height))

while True:
    
    success,img=cap.read()
    
    #opencv bgr alırken hands kütüphanesi rgb istiyor o yüzden convert
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    #hands process et ve multi_had_landmarks ile de eklemlerin kordinatları gör.
    results=hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    #Döngü ile tespiti çizdirelim.
    #Bunun için None ise for döngüsüne girmesin
    if results.multi_hand_landmarks:
        for handslm in results.multi_hand_landmarks:
            #her bir frame de hand landmark işaretlenmesi gerekir.
            #(img,handslm,mpHand.hand_connections(bu bağlantı kurmamızı sağlayacaktır.))
            mpDraw.draw_landmarks(img, handslm,mpHand.HAND_CONNECTIONS)
            
            #eldeki eklemlerin id'lerini ve landmark'larını almak için
            for id, lm in enumerate(handslm.landmark):
                
                #yükselkil,genişlik ve rgb bilgisini alalım image'deki
                h,w,c=img.shape
                
                #kordinat çevirme işlemi yapılır.
                cx,cy=int(lm.x*w),int(lm.y*h)
                
                #parmakların tespiti
                #20 serçe parmagın uç noktası
                if id==20:
                  #circle ile çiz.(img,kordinat,size,renk,içi doldur)
                  cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==19:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==18:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==17:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==16:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==15:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==14:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==13:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==12:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==11:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==10:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==9:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==8:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==7:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==6:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==5:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==4:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==3:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==2:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==1:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                elif id==0:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
                  
                  
    #FPS(frame per seconds hesaplama)
    #algoritmanın ne kadar hızlı çalışıp çalışmadıgını tespit etmek içi kullanılır.
    cTime=time.time()
    fps=1/ (cTime-pTime)
    pTime=cTime
    
    
    #ekranda süreyi görmek için
    cv2.putText(img,"FPS :"+str(int(fps)),(10,75),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),5)
    
    
    
    cv2.imshow("img",img)
    
    writer.write(img)
    
    if cv2.waitKey(1) &0xFF ==ord('q'):
        break
    
cap.release()  # stop capture
writer.release()
cv2.distroyAllWindows()