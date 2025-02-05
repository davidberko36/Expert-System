# import os
# from pyswip import Prolog, Variable

# class PriceEngine:
#     def __init__(self):
#         self.prolog = Prolog()
#         self._find_rules_file()

#     def _find_rules_file(self):
#     # Use raw string and explicit Prolog path formatting
#         rules_path = r"C:\Users\David\Desktop\School\DCIT313\Expert-System\PriceMaker\core\rules.pl"
#         prolog_path = rules_path.replace("\\", "/")  # Convert to Unix-style path
        
#         print(f"Loading rules from: {prolog_path}")
        
#         if not os.path.exists(rules_path):
#             raise FileNotFoundError(f"Rules file missing: {rules_path}")
        
#         try:
#             # Explicitly format consult command
#             consult_cmd = f"consult('{prolog_path}')"
#             # After consult command
#             # test_result = list(self.prolog.query("test_load"))
#             # print("Prolog test query:", test_result)  # Should show [{}] if successful
#             list(self.prolog.query(consult_cmd))  # Force query execution
#             print("✓ Prolog rules loaded")
#         except Exception as e:
#             print(f"! Prolog load error: {str(e)}")
#             raise

#     def calculate_price(self, product):
#         """Accept Product model instance instead of dict"""
#         FinalPrice = Variable()
#         Reasoning = Variable()

#         try:
#             query = (
#                 f"calculate_price("
#                 f"{product.base_cost}, "
#                 f"{product.profit_margin}, "
#                 f"{product.competitor_price}, "
#                 f"'{product.market_demand.lower()}', "
#                 f"'{product.customer_wtp.lower()}', "
#                 f"{'true' if product.is_seasonal else 'false'}, "  # Ensure Prolog-compatible boolean
#                 f"FinalPrice, Reasoning)."  # Correct Prolog variables + add period
#             )


#             print(f"Querying: {query}")

#             results = list(self.prolog.query(query))
#             return {
#                 'price': round(float(results[0][FinalPrice]), 2),
#                 'reasoning': str(results[0][Reasoning])
#             } if results else None

#         except Exception as e:
#             print(f"Query error: {str(e)}")
#             return None


import os
from pyswip import Prolog, Variable

class PriceEngine:
    def __init__(self):
        self.prolog = Prolog()
        self._find_rules_file()

    def _find_rules_file(self):
        rules_path = r"C:\Users\David\Desktop\School\DCIT313\Expert-System\PriceMaker\core\rules.pl"
        prolog_path = rules_path.replace("\\", "/")  # Convert to Unix-style path
        
        print(f"Loading rules from: {prolog_path}")
        
        if not os.path.exists(rules_path):
            raise FileNotFoundError(f"Rules file missing: {rules_path}")
        
        try:
            consult_cmd = f"consult('{prolog_path}')"
            list(self.prolog.query(consult_cmd))  # Force query execution
            print("✓ Prolog rules loaded")
        except Exception as e:
            print(f"! Prolog load error: {str(e)}")
            raise

    def calculate_price(self, product):
        """Accept Product model instance instead of dict"""
        try:
            query = "calculate_price({}, {}, {}, '{}', '{}', {}, FinalPrice, Reasoning)".format(
                product.base_cost,
                product.profit_margin,
                product.competitor_price,
                product.market_demand.lower(),
                product.customer_wtp.lower(),
                "true" if product.is_seasonal else "false"
            )

            print(f"Querying: {query}")

            results = list(self.prolog.query(query))

            return {
                'price': round(float(results[0]['FinalPrice']), 2),
                'reasoning': str(results[0]['Reasoning'])
            } if results else None

        except Exception as e:
            print(f"Query error: {str(e)}")
            return None
