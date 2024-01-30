import cv2 
img = cv2.imread("solar-system.jpg")



cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(210,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(300,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(370,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(600,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(800,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(1000,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1200,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("Display Image",img)

print(img)

cv2.waitKey(0)