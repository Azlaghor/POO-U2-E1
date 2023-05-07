class Email:
    idAcc = ""
    domain = ""
    password = ""
    domType = ""
    
    # Constructor
    def __init__(self, vId, vDom, vDomType, vPass):
        self.idAcc = vId
        self.domain = vDom
        self.domType = vDomType
        self.password = vPass

    # Return Email
    def returnEmail(self):
        return self.idAcc + "@" + self.domain + "." + self.domType

    # Return Domain
    def getDomain(self):
        return self.domain

    # Create Account
    def createAcc(self, email):
        self.idAcc, self.domain = email.split("@")
        self.domain, self.domType = self.domain.split(".")
        self.domType.replace(".", "")