#importing packages
from selenium import webdriver
from save_images import make_directory,save_images,save_data_to_csv
from scrap_images import scrap_image_url
from selenium.common.exceptions import StaleElementReferenceException

#creating a instance for google chrome
Driver_path =r'F:\data sets\chromedriver.exe.exe'

#to run chrome in headfull mode(like regular chrome)
driver= webdriver.Chrome(executable_path=Driver_path)
current_page_url =driver.get('https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/formal-shirt/pr?sid=clo,ash,axc,mmk,bk1&otracker=categorytree&otracker=nmenu_sub_Men_0_Formal%20Shirts')


dir_name='men_shirt'
make_directory(dir_name)

start_page=1
total_pages=3

#scrapping the images
for page in range(start_page,total_pages+1):
    try:
        product_details=scrap_image_url(driver=driver)
        print('scrapping page {0} of {1} pages '.format(page,total_pages))

        page_value=driver.find_element_by_xpath(r"//a[@class='_2Xp0TH fyt9Eu']").text
        print('The current page  scraped is {} '.format(page_value))

        #downlaoding the images
        save_images(data=product_details,dirname=dir_name , page=page)
        print('scrapping of the page {0} done'.format(page))

        #Saving the data into csv file
       # save_data_to_csv(data=product_details,filename='men_tshirt.csv')

        #Moving to the next page
        print('Moving to the next page')
        button_type=driver.find_element_by_xpath("//div[@class='_2zg3yZ']//a[@class='_3fVaIS']//span").get_attribute('innerHTML')

        if button_type=='Next':
            driver.find_element_by_xpath("//a[@class='_3fVaIS']").click()
             
        else:
            driver.find_element_by_xpath("//a[@class='_3fVaIS][2]").click()

        new_page=driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text
        print('The new page is {}'.format(new_page))
  
    except StaleElementReferenceException as Exception:
        print('we are facing an exception')
        exp_page=driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text
        print('The page value at the time pf exception is {}'.format(exp_page))

        value = driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']")
        link=value.get_attribute('href')
        driver.get(link)

        product_details=scrap_image_url(driver=driver)
        print('scrapping page {0} of {1} pages '.format(page,total_pages))

        page_value=driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text
        print('scrapping page {0} of {1} pages '.format(page,total_pages))

        #downlaoding the images
        save_images(data=product_details,dirname=dir_name , page=page)
        print('scrapping of the page {0} done'.format(page))

        #Saving the data into csv file
        #save_data_to_csv(data=product_details,filename='men_tshirt.csv')

        #Moving to the next page
        print('Moving to the next page')
        button_type=driver.find_element_by_xpath("//div[@class='_2zg3yZ']//a[@class='_3fVaIS']//span").get_attribute('innerHTML')

        if button_type=='Next':
            driver.find_element_by_xpath("//a[@class='_3fVaIS']").click()
             
        else:
            driver.find_element_by_xpath("//a[@class='_3fVaIS'][2]").click()

        new_page=driver.find_element_by_xpath("//a[@class='_2Xp0TH fyt9Eu']").text
        print('The new page is {}'.format(new_page))
