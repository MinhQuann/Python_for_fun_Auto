from .base_page import BasePage
from ultils.waits import (
    wait_for_element_to_be_visible,
    Locator,
)

class DashboardPage(BasePage):
    # Locators
    DASHBOARD_TITLE : Locator = (By.XPATH, "//div[contains(@class,'setting__CustomSettingTitle')]")


    # Actions
    def get_all_dashboards(self, min_count: int = 1) -> list[str]:
        # def _ready(d):
        #     els = d.find_elements(*self.DASHBOARD_TITLE)
        #     print(els)
        #     texts = [e.text.strip() for e in els if e.is_displayed() and e.text.strip()]
        #     return texts if len(texts) >= min_count else False
        els =  self.find_elements(self.DASHBOARD_TITLE)
        # texts = []
        # for e in els:
        #     if e.is_displayed() and e.text.strip():
        #         texts.append(e.text.strip())
        #     print(texts)
        # return texts if len(texts) >= min_count else False 
        return [e.text.strip() for e in els if e.is_displayed() and e.text.strip()]
