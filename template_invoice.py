import os
import time
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from selenium.webdriver.support.ui import Select
from datetime import datetime as dt
from datetime import timedelta
from bs4 import BeautifulSoup
import base64
import xml.etree.ElementTree as ET
import requests
import json


class MainPage(WebPage):
    email = WebElement(id='userid')
    password = WebElement(id='password')
    btn = WebElement(id='btnActive')
    left_task_menu = WebElement(xpath='//*[@aria-label="Navigator"]')
    payables_nav = WebElement(xpath='//div[@title="Payables"]')
    invoices_menu = WebElement(xpath='//a[@title="Invoices"]/span')
    right_scroll = WebElement(xpath='//*[@data-icon="navi_caretright"]')
    sem_home = WebElement(xpath='//a[@title="Oracle Logo Home"]')
    payables_nav_menu = WebElement(id='groupNode_payables')
    #purch_req_slide_menu = WebElement(id='itemNode_my_information_purchase_requisitions')
    create_inv_btn = WebElement(xpath='//input[contains(@id,"ct2")]')
    business_unit = WebElement(xpath='//input[contains(@id,"ic2::content")]')
    supplier = WebElement(xpath='//input[contains(@id,"ic3::content")]')
    supplier_site = WebElement(xpath='//input[contains(@id,"ic4::content")]')
    number = WebElement(xpath='//input[contains(@id,"i2::content")]')
    inv_amnt_currency = WebElement(xpath='//input[contains(@id,"soc1::content")]')
    inv_amnt_value = WebElement(xpath='//input[contains(@id,"i3::content")]') #let's check if it's work
    inv_type = WebElement(xpath='//input[contains(@id,"so1::content")]')
    inv_date = WebElement(xpath='//input[contains(@id,"id2::content")]')
    payment_terms = WebElement(xpath='//input[contains(@id,"so3::content")]')
    lines_arrow = WebElement(xpath='//a[contains(@id,"sh2::_afrDscl")]') #or WebElement(xpath='//div[contains (@class,"x6w")]')
    line_amnt = WebElement(xpath='//input[contains(@id,"i26::content")]') #or WebElement(xpath='//span[contains (@id,"i26")]')
    line_distr = WebElement(xpath='//input[contains(@id,"kf1CS::content")]')
    inv_save_btn = WebElement(xpath='//span[contains(text(),"Save")]')
    not_validated = WebElement(xpath='//img[contains(@title,"Status")]')
    inv_actions = WebElement(xpath='//div[contains(@aria-label,"Invoice Actions")]')
    validate_btn = WebElement(xpath='//td[contains(text(),"Validate")]')
    approval_btn = WebElement(xpath='//td[contains(text(),"Approval")]')
    approval_initiate = WebElement(xpath='//td[contains(text(),"Initiate")]')
    logout_icon = WebElement(xpath='//img[@title="Settings and Actions"]')
    signout_click = WebElement(xpath='//a[text()="Sign Out"]')
    confirm_logout = WebElement(xpath='//button[@id="Confirm"]')
    payables_left_menu = WebElement(xpath='//div[@title="Payables"]')
    tools_left_menu = WebElement(xpath='//div[@title="Tools"]')
    invoices_new_menu = WebElement(xpath='//span[text()="Invoices"]')
    worklist_left_menu = WebElement(xpath='//span[text()="Worklist"]')
    
    
    
    category_name = WebElement(xpath='//input[contains(@id,"categoryNameId")]')
    category_name_select = WebElement(xpath='//li[contains(@id,"categoryNameId")]')
    amount = WebElement(xpath='//input[contains(@id,"currencyAmountItemInfo")]')
    currency = WebElement(xpath='//input[contains(@id,"currencyCodeId")]')
    currency_name_select = WebElement(xpath='//li[contains(@id,"categoryNameId")]')
    supplier = WebElement(xpath='//input[contains(@id,"vendorNameId")]')
    supplier_select = WebElement(xpath='//li[contains(@id,"vendorNameId")]')
    add_to_cart = WebElement(xpath='(//a[@role="button"])[2]')
    added_to_card = WebElement(xpath='//span[contains(text(),"Added to Cart")]')
    number_of_PR_in_cart = WebElement(xpath='//span[@class="green large-text bold"]')
    delete_PR_from_cart = WebElement(xpath='//img[@title="Delete"]')
    review_pr = WebElement(xpath='//button[contains(text(), "Review")]')
    service_start = WebElement(xpath='//input[contains(@aria-describedby,"PeriodStart")]')
    service_end = WebElement(xpath='//input[contains(@aria-describedby,"PeriodEnd")]')
    number_of_lines = ManyWebElements(xpath='//td[@_afrrh="true"]')
    submit_pr = WebElement(xpath='(//a[@role="button"])[6]')
    segments = WebElement(xpath='@id, "pt1:_FOr1:0:_FONSr2:0:MAnt2:2:AP1:DelivB:0:disAT:_ATp:distbl:0:kf1CS::content"')
    pr_was_submitted = WebElement(xpath='//div[contains(text(), "Confirmation")]')
    ok_after_submit = WebElement(xpath='//button[@accesskey="K"]')
    first_pr_in_pr_area = WebElement(xpath='//a[contains(text(),"PR")]')
    pr_submitted_number = WebElement(xpath='//div[contains(text(),"PR")]')
    manage_req = WebElement(xpath='//a[text()="Manage Requisitions"]')
    entered_by = WebElement(xpath='//input[@aria-label=" Entered By"]')
    req_no = WebElement(xpath='(//input)[3]')
    created_date = WebElement(xpath='(//select)[3]')
    search_pr = WebElement(xpath='//button[contains(text(),"Search")]')
    pr_in_progress = WebElement(xpath='//a[@title="View the current approval action history"]')
    fin_rep = WebElement(xpath='(//span[contains(text(), "Finance Representative")])')
    fin_rep_names = ManyWebElements(
        xpath='//span[contains(text(), "Finance Representative")]/../span[@style="font-weight:bold"]')
    fa_fin_rep_name = WebElement(
        xpath='(//span[contains(text(), "Finance Representative")]/../span[@style="font-weight:bold"])[2]')
    cost_manager = WebElement(xpath='//span[contains(text(), "Cost Center Manager")]')
    fpna = WebElement(xpath='//span[contains(text(), "FP&A Controller")]')
    fpna_names = ManyWebElements(xpath='//span[contains(text(), "FP&A Controller")]/../span[@style="font-weight:bold"]')
    head_of_fpna = WebElement(xpath='//span[contains(text(), "Head FP&A")]')
    head_of_fpna_name = WebElement(xpath='//span[contains(text(), "Head FP&A")]/../span')
    cfo_name = WebElement(xpath='//span[contains(text(), "CFO")]/../span')
    cfo = WebElement(xpath='//span[contains(text(), "CFO")]')
    segment_select = WebElement(xpath='//img[@title="Select: Charge Account"]')
    team_segment = WebElement(xpath='(//input[contains(@aria-owns,"distbl")])[2]')
    company_segment = WebElement(xpath='(//input[contains(@aria-owns,"distbl")])[1]')
    yes_funds_warning = WebElement(xpath='(//button[text()="Yes"])[2]')
    ok_after_select_segment = WebElement(xpath='//button[@accesskey="k"]')
    # две точки в css это возвращение к родителю, а затем/ вниз к ребенку
    # cost_man2_value = WebElement(xpath='//span[text()="  -  Cost Center Manager"]/../span')
    cost_man_value = WebElement(xpath='//span[text()="  -  Cost Center Manager"]/../span')
    workf_not_av = WebElement(xpath='//h1[contains(text(), "Action Detail")]')
    logout_icon = WebElement(xpath='//img[@title="Settings and Actions"]')
    signout_click = WebElement(xpath='//a[text()="Sign Out"]')
    confirm_logout = WebElement(xpath='//button[@id="Confirm"]')
    tools_tab = WebElement(xpath='//a[text()="Tools"]')
    worklist = WebElement(xpath='//div[@id="ATK_HOMEPAGE_FUSE_WORKLIST"]')
    worklist_search = WebElement(xpath='//input[@type="text"]')
    search_icon = WebElement(xpath='//img[@title="Search"]')
    approve_button = WebElement(xpath='//button[text()="Approve"]')
    reject_button = WebElement(xpath='//button[text()="Reject"]')
    rejection_comment = WebElement(xpath='//textarea')
    reject_submit = WebElement(xpath='//span[text()="Submit"]')
    first_line = WebElement(xpath='(//span[text()="Assigned"])[2]')
    bell_icon = WebElement(xpath='//span[contains(@title,"Notifications")]')
    search_bell = WebElement(xpath='//input[@placeholder="Search"]')
    search_bell_click = WebElement(xpath='//*[@id="pt1:_UISatr:0:cil11::icon"]')
    view_approvals = WebElement(xpath='//button[text()="View Approvals"]')
    PO_click = WebElement(xpath='//a[contains(text(),"PO-")]')
    worklist_not_available = WebElement(xpath='//div[contains(text(),"No tasks are available")]')
    edit_pr_segments = WebElement(xpath='//img[@alt="Edit"]')
    team_dff = WebElement(xpath='//input[contains(@aria-describedby,"RequisitionLineDFFIteratorxxPrcTeam")]')
    office_dff = WebElement(xpath='//input[contains(@aria-describedby,"RequisitionLineDFFIteratorxxPrcOffice")]")]')
    billing_of_pr = WebElement(xpath='//span[contains(text(),"000")]')
    percent_in_pr_line = WebElement(xpath='//input[contains(@name,"Percent")]')
    pr_change_bu_pencil = WebElement(xpath='//img[@alt="Edit"]')
    pr_change_bu_select = WebElement(xpath='//select[contains(@title,"SEMrush")]')
    location_save = WebElement(xpath='//button[@accesskey="S"]')
    done_workflow = WebElement(xpath='//a[@accesskey = "o"]')
    agrm_pr = WebElement(xpath='//input[contains(@id,"agreement")]')
    agrm_po = WebElement(xpath='//span[contains(@id,"agreement")]/..')
    cur_rate = WebElement(xpath='//span[contains(@id,"rate::content")]')
    cur_amount = WebElement(xpath='//span[contains(@id,"amountField")]')
    actions_approval = WebElement(xpath='//a[text()="Actions"]')
    actions_approve = WebElement(xpath='//td[text()="Approve"]')
    purchase_req_left_menu = WebElement(xpath='//div[@title="Procurement"]')
    tools_left_menu = WebElement(xpath='//div[@title="Tools"]')
    purchase_req_new_menu = WebElement(xpath='//span[text()="Purchase Requisitions"]')
    worklist_left_menu = WebElement(xpath='//span[text()="Worklist"]')
    done_manage_pr = WebElement(xpath='//a[@accesskey="o"]')

    pr_count = 0
    company = ''
    team1 = ''
    file_element = 0
    pr_rate = ''
    pr_number = ''
    po_number = ''
    po_agreement = ''
    tasknumber = ''

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://fa-etll-test-saasfaprod1.fa.ocs.oraclecloud.com/'
            super().__init__(web_driver, url)
            self._web_driver.implicitly_wait(15)

    def execute_login(self, email: str, password: str):
        self.email.send_keys(email)
        self.password.send_keys(password)
        select = Select(self._web_driver.find_element_by_xpath('//select[@name="Languages"]'))
        select.select_by_visible_text("English")
        self.btn.click()
        time.sleep(5)

    def open_inv_area(self):
        """ открытие страницы Invoices """

        self.left_task_menu.click()
        self.scroll_down()
        self.payables_left_menu.click()
        time.sleep(2)
        self.invoices_new_menu.click()

    def create_new_invoice(self):
        """создание инвойса"""

        self.create_inv_btn.is_presented()
        self.create_inv_btn.click()

    def enter_inv_header(self, bu, num, amnt, dat):
        """ заполнение хедера инвойса """

        if self.business_unit.is_presented():
            self.business_unit.send_keys(bu)
        else:
            assert False, 'invoice form is not opened'
        if self.supplier_site !='':
            self.number.send_keys(num)
        else:
            assert False, 'supplier is not provided'
        
        self.inv_amnt_value.send_keys(amnt)
        self.inv_date.send_keys(dat)

    def enter_inv_line(self, line_amnt, distr):
        """ добавление строк инвойса """

        self.lines_arrow.click()
        time.sleep(2)

        if self.line_amnt.is_presented():
            self.line_amnt.send_keys(line_amnt)
        else:
            assert False, 'invoice lines are not opened'

        self.line_distr.send_keys(distr)
        self.line_distr.click()


    def save_inv(self)
        """ сохранение инвойса """

        self.inv_save_btn.click()
        time.sleep(5)

        if self.not_validated.is_presented():
            self.number.click()
        else:
            assert False, 'invoice is not saved'

    def validate_inv(self)
        """ валидация инвойса """

        self.inv_actions.click()

        if self.validate_btn.is_presented():
            self.validate_btn.click()
        else:
            assert False, 'validate option is not provided'

    def send_for_approval(self)
        """ инициируем утверждение """

        self.inv_actions.click()

        if self.approval_btn.is_presented():
            self.approval_btn.click()
        else:
            assert False, 'approval option is not provided'

        self.approval_initiate.click()

    def add_pr_to_cart(self):
        """Adding PR to cart"""
        self.add_to_cart.click()

    def fill_agreement(self, agrm):
        """Add agreement to PR"""

        self.scroll_up()
        self.agrm_pr.click()
        self.agrm_pr.send_keys(agrm)

    def click_submit_pr(self):
        """Submit PR with line/lines"""

        self.submit_pr.click()
        self.ok_after_submit.wait_to_be_clickable()
        pr_number_massiv = (self.pr_submitted_number.get_text()).split(' ')
        MainPage.pr_number = pr_number_massiv[1]
        print(MainPage.pr_number)
        self.ok_after_submit.click()

    def open_manage_pr(self):
        """ Open manage requisitions """

        self.manage_req.click()

    def look_for_created_po(self):
        """Look for created PR"""

        self.entered_by.send_keys('')
        self.req_no.send_keys(MainPage.pr_number)
        self.search_pr.click()

    def verify_that_po_was_created(self):
        """Check that PO was created"""

        pr_number_found = self._web_driver.find_element_by_xpath(
            xpath=('//a[contains(text(),"' + MainPage.pr_number + '")]'))
        print('pr_number is', '')
        if pr_number_found != '':
            self.PO_click.wait_to_be_clickable()
            MainPage.po_number = self.PO_click.get_text()

            if MainPage.po_number == '':
                self.done_manage_pr.click()
                print('click on done')
                self.manage_req.click()
                self.entered_by.send_keys('')
                self.req_no.send_keys(MainPage.pr_number)
                self.search_pr.click()
                print('second search')
                if MainPage.po_number != '':
                    print(f"{MainPage.pr_number} was fully approved and {MainPage.po_number} was created")
            else:
                print(f"{MainPage.pr_number} was fully approved and {MainPage.po_number} was created")
        return MainPage.po_number

    def verify_that_po_has_agreement(self):
        """Check that PO has agremeent value"""

        self.PO_click.click()
        time.sleep(6)
        MainPage.po_agreement = self.agrm_po.get_text()
        print(MainPage.po_agreement)
        return MainPage.po_agreement


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


