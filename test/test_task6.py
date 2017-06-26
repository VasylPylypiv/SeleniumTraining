import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_add_new_item():
    driver = webdriver.Firefox()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_class_name('btn.btn-default').click()

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//a[contains(.,'Catalog')]").click()
    driver.find_element_by_xpath("//a[contains(.,' Add New Product')]").click()
    driver.find_element_by_xpath("//label[contains(.,' Enabled')]").click()
    driver.find_element_by_xpath("//label[contains(.,' Unisex')]").click()
    driver.find_element_by_xpath("//input[@name='code']").send_keys("1234567890")
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys("Some new product")
    driver.find_element_by_xpath("//input[@name='sku']").send_keys("1234")
    driver.find_element_by_xpath("//input[@name='gtin']").send_keys("213242")
    driver.find_element_by_xpath("//input[@name='taric']").send_keys("54674")
    driver.find_element_by_xpath("//input[@name='quantity']").clear()
    driver.find_element_by_xpath("//input[@name='quantity']").send_keys("1")
    driver.find_element_by_xpath("//input[@name='weight']").clear()
    driver.find_element_by_xpath("//input[@name='weight']").send_keys("1")
    driver.find_element_by_xpath("//input[@name='dim_x']").clear()
    driver.find_element_by_xpath("//input[@name='dim_x']").send_keys("20")
    driver.find_element_by_xpath("//input[@name='dim_y']").clear()
    driver.find_element_by_xpath("//input[@name='dim_y']").send_keys("30")
    driver.find_element_by_xpath("//input[@name='dim_z']").clear()
    driver.find_element_by_xpath("//input[@name='dim_z']").send_keys("40")
    driver.find_element_by_xpath("//input[@name='date_valid_from']").send_keys("2010-01-01")
    driver.find_element_by_xpath("//input[@name='date_valid_to']").send_keys("2018-01-01")
    driver.find_element_by_xpath("//input[@name='new_images[]']").send_keys(os.getcwd() + "/product.jpeg")
    driver.find_element_by_xpath("//a[@href='#tab-information']").click()
    driver.find_element_by_xpath("//select[@name='manufacturer_id']").click()
    driver.find_element_by_xpath("//option[contains(.,'ACME Corp.')]").click()
    driver.find_element_by_xpath("//input[@name='keywords']").send_keys("gfhgsdjgfsdj")
    driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys("fhhfsdjk")
    driver.find_element_by_xpath("//div[@dir='ltr']").send_keys("fhdjkfsdhjkfh")
    driver.find_element_by_xpath("//textarea[@class='form-control']").send_keys("hgfkjkdgfhkdfj")
    driver.find_element_by_xpath("//input[@name='head_title[en]']").send_keys("djskjdsk")
    driver.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys("hfdjhdj")
    driver.find_element_by_xpath("//button[@name='save']").click()


def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath("//a[contains(.,'Some new product')]")
    except NoSuchElementException:
        return False
    return True
    driver.quit()
