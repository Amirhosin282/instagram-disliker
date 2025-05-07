from config.config import *


# loading                                                                                                                                                             
guess = ''
target = 'AMIRHOSIN282'
for index, character in enumerate(target): # this code for loding animaition                                                                                                            
    j = ord(' ')                                                                                                                                                                        
    while True:                                                                                                                                                                         
        print(f'\r{text(figlet_format(guess, font="slant"))}{text(figlet_format(chr(j), font="slant"))}')                                                                               
        os.system("clear")                                                                                                                                                              
        sys.stdout.flush()                                                                                                                                                              
        sleep(0.00001)                                                                                                                                                                  
        if chr(j) == character:                                                                                                                                                         
            guess += character                                                                                                                                                          
            break                                                                                                                                                                       
        j += 1

view(date_time)

print(Fore.GREEN)

# inputing data from user
user_name = input('print your user name : ').strip()
password = input('print your instagram account password: ').strip()

# open instagram
url = "https://www.instagram.com/"
try:
    driver = webdriver.Chrome()
except:
    print(Fore.RED, 'you dont have any driver, pleas download chrom webdriver or give in my github.')
    sleep(3)
    exit()
# login to your instagram account
driver.get(url)
sleep(3)


# put user name in fild 1 (attacker user name fild)
f1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input"))
)
f1.send_keys(user_name)

# put password in fild 2 (attacker account password)
f2 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input"))
)
f2.send_keys(password)

# click to the login buttom(login on attacker instagram account)
b1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]"))
).click()

# open new tab in chrome and open reel link
sleep(8)
driver.switch_to.new_window('tab')
driver.get("https://www.instagram.com/your_activity/interactions/likes/")
sleep(3)

b2 = WebDriverWait(driver, 13).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div"))
).click()

b3 = WebDriverWait(driver, 13).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/div/span[1]"))
).click()

b4 = WebDriverWait(driver, 13).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div"))
).click()

sleep(8)
while True:
    try:
        b5 = WebDriverWait(driver, 13).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/span"))
        ).click()

        b6 = WebDriverWait(driver, 13).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div"))
        ).click()

        b7 = WebDriverWait(driver, 13).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/article/div/div[2]/div/div/div[1]/div/div/div/div/div[4]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/span"))
        ).click()
        sleep(0.5)
        
        b8 = WebDriverWait(driver, 13).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[1]/div"))
        ).click()
        sleep(5)
    except:
        sleep (5)