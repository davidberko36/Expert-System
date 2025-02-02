% Base price calculation
base_price(Cost, Margin, Price) :-
    Price is Cost * (1 + Margin).


% Demand and WTP based pricing
price_adjustment(high, high, CompetitorPrice, Adjustment) :-
    Adjustment is CompetitorPrice * 0.15.  % Increase by 15%


price_adjustment(high, low, CompetitorPrice, Adjustment) :-
    Adjustment is CompetitorPrice * -0.1.  % Decrease by 5%


price_adjustment(low, low, CompetitorPrice, Adjustment) :-
    Adjustment is CompetitorPrice * -0.1.  % Decrease by 10%


% Seasonal adjustment
seasonal_adjustment(true, BasePrice, Adjusted) :-
    Adjusted is BasePrice * 1.2.
seasonal_adjustment(false, BasePrice, BasePrice).


% Final price calculation
calculate_price(Cost, Margin, CompetitorPrice, Demand, WTP, Seasonal, FinalPrice, Reasoning) :-
    base_price(Cost, Margin, BasePrice),
    price_adjustment(Demand, WTP, COmpetitorPrice, Adjustment),
    NewPrice is BasePrice + Adjustment,
    seasonal_adjustment(Seasonal, NewPrice, FinalPrice),
    determine_reasoning(Demand, WTP, Seasonal, BasePrice, FinalPrice, Reasoning),
    determine_reasoning(Demand, WTP, Seasonal, BasePrice, FinalPrice, Reasoning).


% Reasoning logic
determine_reasoning(high, high, _, _, FinalPrice, 'High demand and WTP justify price increase') :-
    FInalPrice > 0.
determine_reasoning(low, low, _, _, FInalPrice, 'Low demand and WTP suggest price reduction') :-
    FinalPrice >0.