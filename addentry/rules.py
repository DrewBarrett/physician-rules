from business_rules import variables, actions, fields

class ProductVariables(variables.BaseVariables):
    def __init__(self, product):
        self.product = product

    @variables.numeric_rule_variable(label='Age')
    def age(self):
        return self.product.age

    @variables.numeric_rule_variable(label='Rating')
    def rating(self):
        return self.product.rating

    @variables.numeric_rule_variable(label='NPI')
    def npi(self):
        return self.product.npi

    @variables.string_rule_variable(label='Location')
    def location(self):
        return self.product.location

    @variables.string_rule_variable(label='Language')
    def language(self):
        return self.product.language

    @variables.select_rule_variable(label='Board Certified', options=['True','False'])
    def board(self):
        return str(self.product.board_cert)

class ProductActions(actions.BaseActions):
    def __init__(self, product):
        self.product = product

    @actions.rule_action(params={"description": fields.FIELD_TEXT})
    def set_age_results(self, description):
        self.product.age_results = description
        self.product.save()

    @actions.rule_action(params={"description": fields.FIELD_TEXT})
    def set_npi_results(self, description):
        self.product.npi_results = description
        self.product.save()

    @actions.rule_action(params={"description": fields.FIELD_TEXT})
    def set_rating_results(self, description):
        self.product.rating_results = description
        self.product.save()

    @actions.rule_action(params={"description": fields.FIELD_TEXT})
    def set_location_results(self, description):
        self.product.location_results = description
        self.product.save()

    @actions.rule_action(params={"description": fields.FIELD_TEXT})
    def set_language_results(self, description):
        self.product.language_results = description
        self.product.save()

    @actions.rule_action(params={"description": fields.FIELD_TEXT})
    def set_board_cert_results(self, description):
        self.product.board_results = description
        self.product.save()
