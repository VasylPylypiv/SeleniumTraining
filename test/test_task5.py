from selenium import webdriver


def test_litecart_admin_login():
    ff = webdriver.Firefox()
    ff.implicitly_wait(5)
    ff.get("http://localhost/litecart/")
    main_page_name = ff.find_element_by_xpath("//div[@class='name']").text
    main_page_rprice = ff.find_element_by_xpath("//s[@class='regular-price']").text
    main_page_rprice_color = ff.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('color')
    main_page_rprice_text_decoration = ff.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("text-decoration-line")
    main_page_dprice = ff.find_element_by_xpath("//strong[@class='campaign-price']").text
    main_page_dprice_color = ff.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')
    main_page_font_weight = ff.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')
    ff.find_element_by_xpath("(//*[@title='Yellow Duck'])").click()
    item_page_name = ff.find_element_by_xpath("//h1[@class='title']").text
    item_page_rprice = ff.find_element_by_xpath("//del[@class='regular-price']").text
    item_page_rprice_color = ff.find_element_by_xpath("//del[@class='regular-price']").value_of_css_property('color')
    item_page_rprice_text_decoration = ff.find_element_by_xpath("//del[@class='regular-price']").value_of_css_property("text-decoration-line")
    item_page_dprice = ff.find_element_by_xpath("//strong[@class='campaign-price']").text
    item_page_dprice_color = ff.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')
    item_page_font_weight = ff.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')
    print('Product Name is equal on Main page and Item Page - ', main_page_name == item_page_name)
    print('Price discount are equal on both pages - ', main_page_rprice == item_page_rprice)
    print('Prices regular are equal on both pages - ', main_page_dprice == item_page_dprice)
    print('Regular price is gray on both pages - ', main_page_rprice_color == item_page_rprice_color)
    print('Regular price is strike on both pages  - ', main_page_rprice_text_decoration == item_page_rprice_text_decoration)
    print('Campaigns price is red on both pages  - ', main_page_dprice_color == item_page_dprice_color)
    print('Campaigns price is bold on both pages  - ', main_page_font_weight == item_page_font_weight)
    ff.quit()

