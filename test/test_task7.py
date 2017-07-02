from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_litecart_admin_login():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 5)
    #driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/")
    goods_in_cart = int(driver.find_element_by_xpath("//span[@class='quantity']").text)
    #print("Before cycle goods in cart", goods_in_cart)
    for i in range(3):
        driver.find_element_by_xpath("//img[@alt='Yellow Duck']").click()
        driver.find_element_by_xpath("//option[@value='Small']").click()
        driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
        goods_in_cart += 1

        wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"),
                                             str(goods_in_cart)))

        # print("Goods in cart = ", goods_in_cart)
        # print("Goods by web in cart", driver.find_element_by_xpath("//span[@class='quantity']").text)
        driver.find_element_by_xpath("//a[@href='/litecart/']").click()
        wait.until(EC.title_contains("Online"))

    # wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='title']")))
    driver.find_element_by_id('cart').click()

    # for i in range(goods_in_cart):
    WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
    driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()

    driver.quit()
