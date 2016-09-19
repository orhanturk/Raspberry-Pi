#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import smtplib
import ftplib
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEImage import MIMEImage 
from email.Utils import COMMASPACE, formatdate 
from email import Encoders 
from email.mime.text import MIMEText
import subprocess

def sendEmail():
        grab_cam = subprocess.Popen("sudo fswebcam -r 1024x768 kamera.jpg", shell=True)
        grab_cam.wait()  
        image_path = 'kamera.jpg"'
        msg = MIMEText("Testtt")
        COMMASPACE = ','
        msg = MIMEMultipart()
        msg['Subject'] = 'Hareket Algilandi'
        msg['From'] = 'mail@orhsoft.com'
        msg['To'] = 'gönderilecek adres'
        fp = open('kamera.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
        # send email
        s = smtplib.SMTP('mail sunucu',587)
        ##s.starttls()
        s.login('kullanıcı adı', 'parola')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
        
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)


GPIO_PIR = 7

print "Hareket Modulu Test Ediliyor (cikmak icin CTRL-C)"

GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0

try:

  print "Hareket Sensörü Çalışmak için hazır..."

  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "  Hazir"     
    
  while True :
   
    # Hareket Sensörünün Çalışma Algoritması
    Current_State = GPIO.input(GPIO_PIR)
   
    if Current_State==1 and Previous_State==0:
      print "  Hareket Algilandi!"	 
      GPIO.output(27,1)
      time.sleep(15)
      GPIO.output(27,0)
      sendEmail()
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      print "  Hazir"
      Previous_State=0
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Cikis" 
  GPIO.cleanup()