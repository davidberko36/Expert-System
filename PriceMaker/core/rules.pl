% Base price calculation
base_price(Cost, Margin, Price) :-
    Price is Cost * (1 + Margin).

% Price adjustments
price_adjustment(high, high, CompetitorPrice, Adjustment) :-
    Adjustment is CompetitorPrice * 0.15.

price_adjustment(high, low, CompetitorPrice, Adjustment) :-
    Adjustment is CompetitorPrice * -0.05.

price_adjustment(low, low, CompetitorPrice, Adjustment) :-
    Adjustment is CompetitorPrice * -0.10.

price_adjustment(_, _, _, 0).  % Default case

% Seasonal adjustment
seasonal_adjustment(true, Price, AdjustedPrice) :-
    AdjustedPrice is Price * 1.2.
seasonal_adjustment(false, Price, Price).

% Main pricing predicate
calculate_price(Cost, Margin, CompetitorPrice, Demand, WTP, Seasonal, FinalPrice, Reasoning) :-
    base_price(Cost, Margin, BasePrice),
    price_adjustment(Demand, WTP, CompetitorPrice, Adjustment),
    NewPrice is BasePrice + Adjustment,
    seasonal_adjustment(Seasonal, NewPrice, FinalPrice),
    determine_reasoning(Demand, WTP, Seasonal, Reasoning).

% Reasoning rules
determine_reasoning(high, high, _, 'High demand and customer willingness to pay justify price increase').
determine_reasoning(high, low, _, 'High demand but low customer willingness led to cautious pricing').
determine_reasoning(low, low, _, 'Low market demand and customer willingness triggered price reduction').
determine_reasoning(_, _, true, 'Seasonal pricing adjustments applied').
determine_reasoning(_, _, false, 'Standard pricing strategy applied').


% Add at the end of rules.pl
test_load :- write('Prolog rules loaded successfully'), nl.