import requests
class Employee:
    raise_pay=1.05
    def __init__(self,name,family,pay):
        self.name=name
        self.pay=pay
        self.family=family
    @property
    def set_email(self):
        return f"{self.name}.{self.family}@email.com"
    @property
    def fullname(self):
        return f"{self.name} {self.family}"
    def raise_sallary(self):
        result=self.raise_pay*self.pay
        return result
    def monthly_schedule(self,month):
        response=requests.get(f"http://example.com/{self.family}/{month}")
        if response.ok:
            return response.text
        else:
            return "bad Response"
