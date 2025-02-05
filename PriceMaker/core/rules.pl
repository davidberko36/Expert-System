% Base price calculation with a more reasonable formula
base_price(Cost, Margin, Price) :-
    Price is Cost * (1 + (Margin / 100)).  % Margin is now a % of Cost, not an additive number.

% Price adjustment based on market demand and willingness to pay
price_adjustment(high, high, BasePrice, Adjustment) :-
    Adjustment is BasePrice * 0.10.  % Max increase is 10% of base price.

price_adjustment(high, low, BasePrice, Adjustment) :-
    Adjustment is BasePrice * 0.05.  % Conservative increase.

price_adjustment(low, high, BasePrice, Adjustment) :-
    Adjustment is BasePrice * -0.05. % Small discount.

price_adjustment(low, low, BasePrice, Adjustment) :-
    Adjustment is BasePrice * -0.10. % More aggressive discount.

price_adjustment(_, _, _, 0).  % Default case if no condition matches.

% Seasonal price adjustment, now capped at 10% increase
seasonal_adjustment(true, Price, AdjustedPrice) :-
    AdjustedPrice is Price * 1.1.  
seasonal_adjustment(false, Price, Price).

% Ensure price is within a realistic range
reasonable_price(InitialPrice, AdjustedPrice, FinalPrice) :-
    MinPrice is InitialPrice * 0.9,  % Price can only go 10% lower.
    MaxPrice is InitialPrice * 1.5,  % Price can go up to 50% higher, but no more.
    (AdjustedPrice < MinPrice -> FinalPrice = MinPrice;
     AdjustedPrice > MaxPrice -> FinalPrice = MaxPrice;
     FinalPrice = AdjustedPrice).

% Main price calculation rule
calculate_price(Cost, Margin, CompetitorPrice, Demand, WTP, Seasonal, FinalPrice, Reasoning) :-
    base_price(Cost, Margin, BasePrice),
    price_adjustment(Demand, WTP, BasePrice, Adjustment),
    NewPrice is BasePrice + Adjustment,
    seasonal_adjustment(Seasonal, NewPrice, AdjustedPrice),
    reasonable_price(BasePrice, AdjustedPrice, FinalPrice),
    determine_reasoning(Demand, WTP, Seasonal, Reasoning).

% Reasoning rules for final price explanation
determine_reasoning(high, high, _, 'High demand and strong willingness justify a small price increase').
determine_reasoning(high, low, _, 'High demand but low willingness limits price increase').
determine_reasoning(low, high, _, 'Low demand but strong willingness stabilizes pricing').
determine_reasoning(low, low, _, 'Low demand and low willingness result in a moderate price reduction').
determine_reasoning(_, _, true, 'Seasonal pricing adjustments applied').
determine_reasoning(_, _, false, 'Standard pricing strategy applied').

% Ensure the rules file loads correctly
test_load :- write('Prolog rules loaded successfully'), nl.
