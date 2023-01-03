from policyengine_us.model_api import *


class il_aged_blind_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "IL aged and blind exemption"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        aged_blind_count = tax_unit("aged_blind_count", period)
        return (
            aged_blind_count
            * parameters(
                period
            ).gov.states.il.tax.income.exemption.aged_and_blind
        )
