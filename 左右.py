# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:12:46 2021

@author: User
"""

import numpy as np
import random 

class piano_right_hand:
    def __init__(self,setting):
        self.setting=setting
        
        self.chord_c = [ "c'","d'", "e'", "g'","bis'","rand"]
        self.chord_f = [ "f'","g'", "a'", "c'","e'" ,"rand" ]
        self.chord_g = [ "g'","a'", "b'", "d'","f'" ,"rand" ]
        self.chord_e = [ "e'","aes'", "b'", "d'" , "f'" ,"rand" ]
        
        self.chord_am = [ "a'","b'", "c'", "e'","g'"  ,"rand" ]
        self.chord_dm = [ "d'","e'", "f'", "a'","c'"  ,"rand" ]
        self.chord_em = [ "e'","f'", "g'", "b'","d'" ,"rand" ]
        
    def randomBeats( self,totalbeat, QuarterNote1,QuarterNote2, TheAmountOfOutputBeats):
        nrandom=0
        num=0
        i=0
        beatssec=0.0
        nsum=0.0
        OutputBeats = [""] * 100
        
        
        beatarr=np.zeros(100)
        
        arr=[totalbeat / 1.0 , totalbeat / 2.0 , totalbeat / 2.0 + totalbeat / 4.0 , totalbeat / 4.0 , totalbeat / 8.0 , totalbeat / 16.0 ,totalbeat / 32.0]
        count=0
        while 1:
            for j in range(TheAmountOfOutputBeats):
                beatarr[j]=0
            nsum=0
            num=0
            
            while 1:
                if num > TheAmountOfOutputBeats:
                    break
                nrandom = random.randint(QuarterNote1,QuarterNote2) 
                beatssec = arr[nrandom]
                
                if nsum + beatssec <= totalbeat:
                    nsum += beatssec
                    beatarr[num] = nrandom
                    num+=1
                
                if nsum == totalbeat:
                    break
            
            if num == TheAmountOfOutputBeats:
                break
            if count>10000:
                return -77777777,OutputBeats
            count=count+1
        
        for i in range(num):
            n=beatarr[i]
            if   n==0:
                OutputBeats[i] = "1"
            elif n==1:
                OutputBeats[i] = "2"
            elif n==2:
                OutputBeats[i] = "2."
            elif n==3:
                OutputBeats[i] = "4"
            elif n==4:
                OutputBeats[i] = "8"
            elif n==5:
                OutputBeats[i] = "16"
            elif n==6:
                OutputBeats[i] = "32"
        
        return num,OutputBeats
    
    
    
    def Chord(self,str,number):
        if   str=="c":
            return self.chord_c[number]
        elif str=="f":
            return self.chord_f[number]
        elif str=="g":
            return self.chord_g[number]
        elif str=="am":
            return self.chord_am[number]
        elif str=="dm":
            return self.chord_dm[number]
        elif str=="em":
            return self.chord_em[number]
        elif str=="e":
            return self.chord_e[number]
        return "exit"
    
    
    
    def sort(self,N):   #0-N隨機排列
        arr=[0]*N
        for i in range(N):
            nout=True
            while nout:
                n=random.randint(0,N)
                nout=False
                for j in range(i):
                    if arr[j]==n:
                        nout=True
                        break
            arr[i]=n
        return arr
    
    
    def melody(self,chrd_arr,arraylength,Sent):
        bar=0
        note=0
        note_n=0
        sent=0
        
        for sent in range(Sent):
            r=self.setting["rh_TheAmountOfOutputBeats"][sent]
    
            #outputbeats=[""]*100
            num= -77777777
            
            while num == -77777777:
                num,outputbeats = self.randomBeats(self.setting["totalbeat"], self.setting['rh_QuarterNote1'], self.setting['rh_QuarterNote2'], r)  #總拍子數    幾分音符    輸出幾個beats    OutputBeats[]
                
            for bar in range(arraylength):
                note_n = num
                for note in range(note_n):
                    
                    Chordstr= self.Chord(chrd_arr[bar], random.randint(0,5) )
                    
                    if Chordstr=="rand":
                        arr=self.sort(4)
                        print("<",end="")
                        
                        for i in range(random.randint(1,4)):
                            print(self.Chord(chrd_arr[bar], arr[i ])," ",end="")
                        print(">",end="")
                    else:
                        print(Chordstr,end="")
                    
                    print(outputbeats[note]," ",end="")
                print("\n",end="")
            print("\n\n",end="")
        
        print("c''1",end="")
        return 0
    

        
    
    def display(self,chrd_arr,arraylength, Sent):
    
        self.melody(chrd_arr, arraylength, Sent)
        


class piano_left_hand:
    def __init__(self,setting):
        self.setting=setting
        self.chord_c = [ "c", "e", "g"]
        self.chord_f = [ "c", "f", "a" ]
        self.chord_g = [ "d","g","b" ]
        self.chord_e = [ "e","gis", "b" ]
        
        self.chord_am = [ "c",  "e","a" ]
        self.chord_dm = [ "d", "f", "a" ]
        self.chord_em = [ "e", "g", "b" ]


    def mutiNote(self,chord,num):
        if num==0:
            return chord[0]
        elif num==1:
            return chord[1]
        elif num==2:
            return chord[2]
        elif num==3:
            return "<"+chord[0]+" "+ chord[1]+">"
        elif num==4:
            return "<" + chord[0] + " " + chord[2] +">"
        elif num==5:
            return "<" + chord[1] + " " + chord[2] +">"
        elif num==6:
            return "<" + chord[0] + " " + chord[1] +" " + chord[2] +">"
    
    def randomBeats(self, totalbeat, QuarterNote1,QuarterNote2, TheAmountOfOutputBeats):
        nrandom=0
        num=0
        i=0
        beatssec=0.0
        nsum=0.0
        OutputBeats = [""] * 100
        
        
        beatarr=np.zeros(100)
        
        arr=[totalbeat / 1.0 , totalbeat / 2.0 , totalbeat / 2.0 + totalbeat / 4.0 , totalbeat / 4.0 , totalbeat / 8.0 , totalbeat / 16.0 ,totalbeat / 32.0]
        count=0
        while 1:
            for j in range(TheAmountOfOutputBeats):
                beatarr[j]=0
            nsum=0
            num=0
            
            while 1:
                if num > TheAmountOfOutputBeats:
                    break
                nrandom = random.randint(QuarterNote1,QuarterNote2) 
                beatssec = arr[nrandom]
                
                if nsum + beatssec <= totalbeat:
                    nsum += beatssec
                    beatarr[num] = nrandom
                    num+=1
                
                if nsum == totalbeat:
                    break
            
            if num == TheAmountOfOutputBeats:
                break
            if count>10000:
                return -77777777,OutputBeats
            count=count+1
        
        for i in range(num):
            n=beatarr[i]
            if   n==0:
                OutputBeats[i] = "1"
            elif n==1:
                OutputBeats[i] = "2"
            elif n==2:
                OutputBeats[i] = "2."
            elif n==3:
                OutputBeats[i] = "4"
            elif n==4:
                OutputBeats[i] = "8"
            elif n==5:
                OutputBeats[i] = "16"
            elif n==6:
                OutputBeats[i] = "32"
        
        return num,OutputBeats
    
    
    
    def Chord(self,str,number):
        if   str=="c":
            return self.mutiNote(self.chord_c,number)
        elif str=="f":
            return self.mutiNote(self.chord_f,number)
        elif str=="g":
            return self.mutiNote(self.chord_g,number)
        elif str=="am":
            return self.mutiNote(self.chord_am,number)
        elif str=="dm":
            return self.mutiNote(self.chord_dm,number)
        elif str=="em":
            return self.mutiNote(self.chord_em,number)
        elif str=="e":
            return self.mutiNote(self.chord_e,number)
        return "exit"
    
    
    
    def sort(self,N):   #0-N隨機排列
        arr=[0]*N
        for i in range(N):
            nout=True
            while nout:
                n=random.randint(0,N)
                nout=False
                for j in range(i):
                    if arr[j]==n:
                        nout=True
                        break
            arr[i]=n
        return arr
    
    
    def melody(self,chrd_arr,arraylength,Sent):
        bar=0
        note=0
        note_n=0
        sent=0
        
        for sent in range(Sent):
            r=self.setting['lh_TheAmountOfOutputBeats'][sent]
    
            #outputbeats=[""]*100
            num= -77777777
            
            while num == -77777777:
                num,outputbeats = self.randomBeats(self.setting["totalbeat"], self.setting["lh_QuarterNote1"],self.setting["lh_QuarterNote2"], r)  #總拍子數    幾分音符    輸出幾個beats    OutputBeats[]
            
            
            chordarr=[0]*100
            for I in range(100):
                chordarr[I] =random.randint(0,6)
            
            
            for bar in range(arraylength):
                note_n = num
                for note in range(note_n):
                    
                    print(self.Chord(chrd_arr[bar], chordarr[note]),end="")
                    #Chordstr= Chord(chrd_arr[bar], random.randint(0,5) )
                    
                    #if Chordstr=="rand":
                        #arr=sort(4)
                        #print("<",end="")
                        
                        #for note in range(note_n):
                            #print(Chord(chrd_arr[bar], chordarr[note])," ",end="")
                        #print(">",end="")
                    #else:
                        #print(Chordstr,end="")
                    
                    print(outputbeats[note]," ",end="")
                print("\n",end="")
            print("\n\n",end="")
        
        print("c1",end="")
        return 0
    
    
    
    
    
        
    
    def display(self,chrd_arr,arraylength, Sent):
    
        self.melody(chrd_arr, arraylength, Sent)

def lilyshow(setting):
    length =len(setting['chrd_arr'])
    prh=piano_right_hand(setting)
    plh=piano_left_hand(setting)
        
    print('''\\header {
      title = "Untitled"
      composer = "Composer"
    }
    
    \\score {
      <<
      \\new Staff { \\clef "treble" \\key d \\major \\time 4/4 
                   \\tempo 4 = ''',end='')
    print(setting['tempo'])
    prh.display(setting['chrd_arr'], length,setting['Sent'])
        
    print('''
              }
      \\new Staff { \clef "bass" 
                  '''
                  )
    plh.display(setting['chrd_arr'], length,setting['Sent'])
    print('''}
    >>
    
      \\layout {}
      \\midi {}
    }''')
    
#a,b=randomBeats(4,6,8)  # 總拍子數    幾分音符    輸出幾個beats    
            
def getSentByLen(rh_TAO,lh_TAO):
    
    a=len(rh_TAO)
    b=len(lh_TAO)
    
    if a==b:
        return a
    else:
        return 'err'
    



if __name__ == '__main__':
    #chrd_arr = [ "f","g","em","am","dm","g","c","c"]  "c","g","am","em"
    
    Tempo=120
    
    chrd_arr =["f","g","em","am","dm","g","c","c"] #設定和弦
    rh_TheAmountOfOutputBeats=[7,9,7,9,7]  #設定每一段的音符數
    lh_TheAmountOfOutputBeats=[6,6,6,6,6]  #設定每一段的音符數 
    
    #QuarterNote  幾分音符(0:全音符 1:2分音符  2:3分音符  3:4分音符  4:8分音符  5:16分音符  6:32分音符)
    rh_QuarterNote_upper=5  #右手要開的音符數(最高
    rh_QuarterNote_lower=3  #右手要開的音符數(最低
    
    lh_QuarterNote_upper=4  #左手要開的音符數(最高
    lh_QuarterNote_lower=0  #左手要開的音符數(最低
    
    sent=getSentByLen(rh_TheAmountOfOutputBeats,lh_TheAmountOfOutputBeats)  #與上面的rh_TAO、lh_TAO陣列長度相同
    
    #totalbeat 總拍子數  , 
    setting={'totalbeat':4,'tempo':Tempo,'rh_QuarterNote1':rh_QuarterNote_lower,'rh_QuarterNote2':rh_QuarterNote_upper,'lh_QuarterNote1':lh_QuarterNote_lower,'lh_QuarterNote2':lh_QuarterNote_upper,'Sent':sent,'chrd_arr':chrd_arr,'lh_TheAmountOfOutputBeats':lh_TheAmountOfOutputBeats,'rh_TheAmountOfOutputBeats':rh_TheAmountOfOutputBeats}
   
    lilyshow(setting)
    
    
   