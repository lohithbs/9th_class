from selenium import webdriver
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('https://jqueryui.com/datepicker/#dropdown-month-year')
driver.maximize_window()
driver.implicitly_wait(10)
ele=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)
driver.find_element_by_id("datepicker").send_keys("08/04/2020",Keys.ENTER)




# e_d="22"
# e_m="2"
# e_y="2020"
# driver.find_element_by_id("datepicker").click()
# year_ele=Select(driver.find_element_by_xpath("//select[@class='ui-datepicker-year']"))
# year_ele.select_by_visible_text(e_y)
# month_ele=Select(driver.find_element_by_xpath("//select[@class='ui-datepicker-month']"))
# month_ele.select_by_value(e_m)
# f_x="//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()="
# s_x=""
# t_x=""
# ff_x="]"
# final_x=f_x+s_x+e_d+t_x+ff_x
# print(final_x)
# driver.find_element_by_xpath(final_x).click()
#
