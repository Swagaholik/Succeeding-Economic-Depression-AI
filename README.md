# Succeeding-Economic-Depression-AI
Uses Artificial Intelligence to formulate and model how to reach a goal state of economic upswing from a start state of economic recession. Also includes work with solving Fox-Farmer-Chicken problem using AI. 

Part A:

Nodes on the solution path:

People in left bank (starting position): Farmer Fox Chicken Grain People in right bank (destination):

People in left bank (starting position): Fox Grain People in right bank (destination): Farmer Chicken

People in left bank (starting position): Fox Grain Farmer People in right bank (destination): Chicken

People in left bank (starting position): Grain

People in right bank (destination): Chicken Farmer Fox

People in left bank (starting position): Grain Farmer Chicken People in right bank (destination): Fox

People in left bank (starting position): Chicken People in right bank (destination): Fox Farmer Grain

People in left bank (starting position): Chicken Farmer People in right bank (destination): Fox Grain

People in left bank (starting position):

People in right bank (destination): Fox Grain Farmer Chicken

Length of solution path found: 7 edges

Part B:

Wicked Problem Chosen: Avoiding a severe economic depression in the United States.

Problem Breakdown:
The Severe US Economic Depression problem is modeled around the Great Depression
of the late 20s to early 30s, as well as the 2008 economic recession. For this wicked problem,
we will start at a state where the US is undergoing severe economic depression (we have unemployment and inflation rates high enough that constitute those of an economic depression). Our goal state is
to try and reduce both of these rates (unemployment and inflation) until we are at economic upswing standards. Our goal is to try and reach this goal state in the least number of years (starting at the year 2020). Each year, we are given three options of actions to take in order to reduce either the country's unemployment rate (which may increase the country's inflation rate) or reduce the country's inflation rate (which may increase the country's unemployment rate). When we reach the unemployment rate and inflation rate of economic upswing standards (opposite of economic depression), then we win. The three options we have to choose from every year is to increase government spending (which will decrease unemployment and increase inflation rates), invest in banks (which will increase unemployment and decrease inflation rates), and reduce taxes (which will decrease unemployment and increase inflation). Some rules that must be followed when choosing an action every year are that (1) the government cannot choose to make the same action every year, (2) the unemployment rate cannot spill over a 20% threshold, and (3) the inflation rate cannot spill over a 15% threshold, (4) if a certain rate is already below the threshold for economic upswing then we must choose the action that prioritizes the reduction of the other rate.

Factors:
- Unemployment rate – 15% for depression state, 3% for economic upswing
- Inflation – 10% for depression state, -10% for economic upswing
Actions:
- Increase Government Spending
o decreases unemployment rate by 1.5%
o increases inflation by 0.6%
- Bank Investments (Gov’t investing in banks for financial stability)
o Increases unemployment by 0.4%
o Decreases inflation by 2.2%
- Reduce Taxes (Increase consumer spending)
o Decreases unemployment by 1.9% o Increases inflation by 0.8%
Rules:
- Cannot perform the same government action two years in a row
- Unemployment cannot go over 20%
- Inflation cannot go over 15%
Evaluation Function:
Q(s) = (Current State Unemployment Rate – Unemployment Rate for Economic Upswing) +
(Current State Inflation Rate – Inflation Rate for Economic Upswing)

The lower our Q(s) evaluation is, the better (the closer we are to the goal state). This is because our Q(s)
evaluates how much higher our current unemployment and inflation rates are from the ideal (lower)
unemployment and inflation rates that match those of our goal state (those of the United States in an
economic upswing). For example, in the start state (i.e. when the US is in severe economic depression
because that’s where we start in this problem), our initial unemployment and inflation rates are 15% and
10%, respectively. By evaluating our Q(s), we find that we are (15-3) + (10-(-10)) = 12 + 20 = 32 units away
from reaching our goal state, which relatively is not good since the worse Q(s) function we can have given our
unemployment/inflation rate thresholds is Q(s) = (20-3) + (15-(-10)) = 17 + 25 = 42. So an economic break-
even point would be when Q(s)=~42/2=approximately 21 units.

Demonstration Sequences:

DFS algorithm state sequences to solution:

Solution path:

Current Unemployment Rate: 15% Current Inflation Rate: 3%

Last Government Action Taken:

Current Unemployment Rate: 13.5%

Current Inflation Rate: 3.6%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 13.9%

Current Inflation Rate: 1.4%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 12.4%

Current Inflation Rate: 2.0%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 12.8%

Current Inflation Rate: -0.20000000000000018%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 11.3%

Current Inflation Rate: 0.3999999999999998%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 11.700000000000001%

Current Inflation Rate: -1.8000000000000003%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 10.200000000000001%

Current Inflation Rate: -1.2000000000000002%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 10.600000000000001%

Current Inflation Rate: -3.4000000000000004%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 9.100000000000001%

Current Inflation Rate: -2.8000000000000003%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 9.500000000000002%

Current Inflation Rate: -5.0%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 8.000000000000002%

Current Inflation Rate: -4.4%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 8.400000000000002%

Current Inflation Rate: -6.6000000000000005%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 6.900000000000002%

Current Inflation Rate: -6.000000000000001%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 7.3000000000000025%

Current Inflation Rate: -8.200000000000001%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 5.8000000000000025%

Current Inflation Rate: -7.600000000000001%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 6.200000000000003%

Current Inflation Rate: -9.8%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 4.700000000000003%

Current Inflation Rate: -9.200000000000001%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 5.100000000000003%

Current Inflation Rate: -11.400000000000002%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 3.600000000000003%

Current Inflation Rate: -10.800000000000002%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 1.7000000000000033%

Current Inflation Rate: -10.000000000000002%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Length of solution path found: 20 edges 20 states expanded. MAX_OPEN_LENGTH = 21

BFS algorithm state sequences to solution:

Nodes on the solution path:

Current Unemployment Rate: 15% Current Inflation Rate: 3%

Last Government Action Taken:

Current Unemployment Rate: 13.5%

Current Inflation Rate: 3.6%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 13.9%

Current Inflation Rate: 1.4%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 12.4%

Current Inflation Rate: 2.0%

Last Government Action Taken: Increase Government Spending to Increase Welfare

Current Unemployment Rate: 12.8%

Current Inflation Rate: -0.20000000000000018%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 10.9%

Current Inflation Rate: 0.5999999999999999%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 11.3%

Current Inflation Rate: -1.6000000000000003%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 9.4%

Current Inflation Rate: -0.8000000000000003%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 9.8%

Current Inflation Rate: -3.0000000000000004%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 7.9%

Current Inflation Rate: -2.2%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 8.3%

Current Inflation Rate: -4.4%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 6.4%

Current Inflation Rate: -3.6000000000000005%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 6.800000000000001%

Current Inflation Rate: -5.800000000000001%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 4.9%

Current Inflation Rate: -5.000000000000001%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 5.300000000000001%

Current Inflation Rate: -7.200000000000001%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 3.400000000000001%

Current Inflation Rate: -6.400000000000001%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 3.8000000000000007%

Current Inflation Rate: -8.600000000000001%

Last Government Action Taken: Invest in Banks for Financial Stability

Current Unemployment Rate: 1.9000000000000008%

Current Inflation Rate: -7.800000000000002%

Last Government Action Taken: Reduce Taxes to Stimulate Consumer Spending

Current Unemployment Rate: 2.3000000000000007%

Current Inflation Rate: -10.000000000000002%

Last Government Action Taken: Invest in Banks for Financial Stability

Length of solution path found: 18 edges 2646 states expanded. MAX_OPEN_LENGTH = 374

From above, we can see what changes in every state with every operator. When we use the INCREASE_GOVT_SPENDING (“Increase Government Spending to Increase Welfare”) operator, our Unemployment rate decreases by 1.5 units (inflation rate in economy decreases) and our Inflation rate increases by 0.6 units. When we use the INVEST_IN_BANKS (“Invest in Banks for Financial Stability”) operator, our Unemployment rate increases by 0.4 units and our Inflation rate decreases by 2.2 units. And when we use the REDUCE_TAXES (“Reduce Taxes to Stimulate Consumer Spending”) operator, our Unemployment rate decreases by 1.9 units and our Inflation rate increases by 0.8 units.

Summary:

In this problem, I attempted to capture how long it would take to go from the worst economic situations the US has ever been to the very best (i.e. go from the historically lowest unemployment and inflation rates in the US to historically the best respective rates). Since it has already been researched that it takes approximately 8 years for the US to climb out of a recession, I wanted to see how long it would take to go from the very worst situation (severe economic depression) to the very best (economic upswing) instead of a relatively bad situation (a recession) to a break-even (neutral) economy. In formulating the problem, I made the three actions the government could take per year based around what I researched were the three main ways a government can expand overall national GDP and climb out of economic depression. For the three Government Actions, I chose the influence each action had on unemployment and inflation rates as a conservative average of the change they make on unemployment and inflation rates using past annual US unemployment and inflation rates. I believe that for the most part, my problem formulation was successful in capturing a ballpark of the years it would take for the economy to completely switch from an economic depression to economic boom (18 years when using BFS search algorithm and 20 years when using DFS search algorithm). This was what was generally expected, however, I do believe that having constant changes in unemployment and inflation rates for each Government Action simplified the problem more than what is usually realistically exhibited in the US economy. Another problem with my problem formulation was that to make the rules more viable to a “wicked problem”, I made it so that all of the calculations in the evaluations of states and changes in the problem were linear, which also constitutes making the annual Government Actions have constant changes to unemployment and inflation rates. Although these actions had constant changes that were just the average of what sort of impact they would have on the US economy (based on past US economic changes), I still believe, however, that they were a good capture of how the US economy shifts when performing these actions. This is because in the final solution paths for BFS and DFS, increasing government spending to increase welfare was a more frequent action chosen to reduce unemployment rates than reducing taxes was. This is because reducing taxes would have created more of a problem with inflation than it did long-term good for decreasing unemployment rates (at least in comparison to that of increasing government spending and welfare). Another main problem with my formulation was that it only had three total Government Actions to choose from every year, which isn’t realistic to the US’s real economic mobilization, as the US can not only make more than one annual economic decision, but has more than just 3 constant actions to choose from. Another interesting factor that could have been added to my problem formulation was to add international affairs to the US’s economic evaluation. This could have been an interesting factor to simulate, considering the US’s economic boom post-WWII could attest to the fact that US international affairs and policy does impact domestic economy. Nevertheless, for an isolated and observed simulation, I think my problem formulation best captured what steps the government needs to take (based off the three most important actions I researched) to achieve economic boom in the shortest amount of time (with my numbers being averaged across past observed US economic factors).

References:

- For complete history of US Unemployment Rates since 1914: https://tradingeconomics.com/united-states/unemployment- rate#:~:text=Unemployment%20Rate%20in%20the%20United,percent%20in%20May%20of%201953 .
- For complete history of US Inflation Rates since 1914: https://tradingeconomics.com/united- states/inflation-cpi#:~:text=Inflation%20Rate%20in%20the%20United,percent%20in%20June%20of%201921.
- For seeing annual changes of inflation rates, GDP growth, and causation of annual economic changes
in US since 1929: https://www.thebalance.com/unemployment-rate-by-year-3305506
- For seeing specifically what the highest monthly inflation rates were during the Great Depression
and for seeing some speculations as to what Government Actions caused the Great Depression:
https://inflationdata.com/articles/inflation-cpi-consumer-price-index-1930-1939/
- For seeing ways we can avoid another economic depression and how specifically these Government Actions help the economy: https://corporatefinanceinstitute.com/resources/knowledge/economics/economic-depression/
