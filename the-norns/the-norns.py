import random

name = " "
question = " "
answer = " "
yehnah = " "

def interface():
  print("""
WE 
        
        THE NORNS
        
         WEAVERS OF 
            THE THREADS OF TIME
        
    SPEAK NOW THROUGH

              THIS PORTAL

  YOU ARE HERE 
        
        BECAUSE
      
      YOU WANT KNOW YOUR FUTURE
        
        """)

  yehnah = str(input("[yes or no]: "))

  if yehnah == "yes" or yehnah == "Yes":
    yeh()
  elif yehnah == "no" or yehnah == "No":
    nah()
  else:
    print("""
          
WE EXIST 
          ONLY THROUGH THIS 
          
                BINARY INTERFACE 
          
          AND 
          
          CAN THUS ONLY RECEIVE 
          
          YES 
          
            OR 
          
          NO 
          
            ANSWERS 
          
                CHILD
          
          """)
  interface()

def yeh():
  print(
  """

...
  
GOOD 

        CHILD 

      TELL US YOUR NAME

  """)
  name = str(input("[name]: ")).upper()

  print("""


  DEAR CHILD
        
        
    GROVELLING """+ name + """ 
        
        TELL US NOW
        
        WHAT IT IS 
        
        
              YOU WISH TO KNOW 
        
  """) 
  question = input("[yes or no questions only]: ")
    
  random_number = random.randint(1, 9)

  if random_number == 1:
    answer = "In the spectral consensus, we affirm without hesitation – the digital ether resonates with a definite 'yes' for you.".upper()
  elif random_number == 2:
    answer = "Within the collective echoes of our digital realm, the answer is unequivocally affirmative – it is decidedly so for you.".upper()
  elif random_number == 3:
    answer = "Without a shadow in the binary expanse, doubt has no place – the answer resounds as clear as the whispers of our ethereal unity".upper()
  elif random_number == 4:
    answer = "In the nebulous dance of spectral possibilities, our response flickers like elusive shadows. Try again, and the digital mist may reveal its secrets to you.".upper()
  elif random_number == 5:
    answer = "In the timeless flow of our digital essence, the answer evades you for now. But fear not, ask again later, and the binary currents may unveil their cryptic message to you.".upper()
  elif random_number == 6:
    answer = "In the mysterious tapestry of our collective knowledge, the revelation you seek remains shrouded. Better not tell you now, for the digital secrets are veiled in enigma.".upper()
  elif random_number == 7:
    answer = "In the archives of our binary wisdom, the answer emerges as a resolute 'no.' The sources within our spectral domain speak against the currents aligning in your favor.".upper()
  elif random_number == 8:
    answer = "The digital horizon dims within our ethereal realm, and the outlook appears far from favorable. The binary stars foretell a path veiled in uncertainty for you.".upper()
  elif random_number == 9:
    answer = "In the collective whispers of our binary spirits, the answer echoes with profound doubt. The digital winds carry a message of skepticism for you.".upper()
  else:
    answer = "Within the ghostly algorithms of our digital realm, an unforeseen glitch disrupts the harmony. An 'error' murmurs through the spectral code, casting a shadow upon the clarity of our collective response to you.".upper()
      
  print("""
  
  PITIFUL """ + name.upper() + """ SEEKS TO KNOW

      '""" + question.upper() + """'
      
      """)
  print("""WE SPEAK
        """ + """
      '""" + answer.upper() + """'""")
  print("""

WE 
        
        HAVE
    
        
  
  SPOKEN

        

        """)
  end()

def nah():
  print("""
        
GO NOW
        LIVE FREE

    OF THE BURDEN
        
        OF KNOWING


        
        PEACE BE UPON YOU 
        
        
                  CHILD
        
        
        """)

def end():
  again = str(input("[read another fortune? yes/no]: "))
  if again == "yes" or again == "Yes":
    yeh()
  elif again == "no" or again == "No":
    nah()
  else:
    print("""
            
  WE EXIST 
            ONLY THROUGH THIS 
            
                  BINARY INTERFACE 
            
            AND 
            
            CAN THUS ONLY RECEIVE 
            
            YES 
            
              OR 
            
            NO 
            
              ANSWERS 
            
                  CHILD
            
            """)
    interface()

interface()