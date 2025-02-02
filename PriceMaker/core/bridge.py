from pyswip import Prolog
import os

class PriceEngine:
    def __init__(self):
        self.prolog = Prolog()
        rules_path = os.path.join(os.path.dirname(__file__), 'rules.pl')
        self.prolog.consult(rules_path)

    def calculate_price(self, product):
        query = (f'calculate_price({product.base_cost}, {product.profit_margin}, '
                 f"{product.competitor_price}, {product.market_demand.lower()}, "
                 f"{product.customer_wtp.lower()}, {str(product.is_seasonal).lower()}, "
                 f"FinalPrice, Reasoning)")
        
        result = list(self.prolog.query(query))
        if result:
            return {
                'price': round(result[0]['FInalPrice'], 2),
                'reasoning': result[0]['Reasoning']
            }
        return None