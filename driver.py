import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def main(argv):
    url = 'http://www.watchcartoononline.com/darker-than-black-episode-1-english-dubbed'
    if len(argv) >= 1:
        url = argv[0]
    adblockfile = "./adblock.xpi"

    next = lambda x : x.find_element_by_xpath("//body//a[@rel='next']").click()

    ffprofile = webdriver.FirefoxProfile()
    ffprofile.add_extension(adblockfile)
    driver = webdriver.Firefox(ffprofile)
#driver.maximize_window()
    driver.get(url)
#driver.find_element_by_tag_name("html").send_keys(Keys.F11)
    while True:
        url = driver.current_url
        iframe = driver.find_element_by_id("frameNewcizgifilmuploads0").get_attribute('src')
        driver.get(iframe)
        driver.find_element_by_xpath("//input[@id='yuklen']").click()
        sleep(1)
        driver.execute_script("document.body.style.overflow = 'hidden';")
        driver.execute_script("jwplayer().play();")
        driver.execute_script("jwplayer().resize('100%', '100%');")
        sleep(5)
        status = ""
        while(status != "IDLE"):
            status = driver.execute_script("return jwplayer().getState();")
        driver.get(url)
        try:
            next(driver)
        except:
            break

    driver.close()

if __name__ == '__main__':
    main(sys.argv[1:])
