from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def login(email, password):
    # try:
      url2  = 'https://www.zoho.com/people/?zsrc=fromproduct#home/dashboard'
      url1 = "https://accounts.zoho.com/signin?servicename=zohopeople&signupurl=https://www.zoho.com/people/signup.html"

      chrome_options = webdriver.ChromeOptions()
      # chrome_options.add_argument("--headless")
      chrome_options.add_argument("--disable-gpu")
      chrome_options.add_argument("--no-sandbox")
      chrome_options.add_argument('--disable-dev-shm-usage')

      driver  = webdriver.Chrome(options=chrome_options)
      
      driver.get(url1)

      # login wiith mail
      # WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'login_id'))).send_keys(f'{email}\n')
      # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(f'{password}\n')


      # login with google
      driver.find_element(By.CLASS_NAME, "google_icon").click()

      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(f'{password}\n')
      sleep(5)


      # driver.find_element(By.ID, "ZPD_Top_Att_Stat").click()
      try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'ZPD_Top_Att_Stat'))).click()
      except:
        try:
          driver.get(url2)
          WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'ZPD_Top_Att_Stat'))).click()
        except Exception as err:
          print(err)

      print("Atendace Marked")    
      sleep(8)

      driver.save_screenshot('screenie.png')
      driver.close()
     
      return 'Done'
    # except Exception as err:
    #   driver.save_screenshot('screenie.png')
    #   return str(err)



                                                                                  
if __name__ == "__main__":

  email = 'emi123noel@gmail.com'
  password = 'Zoho123!'

  login(email, password)  
