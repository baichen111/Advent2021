i:flip read0`:Part1Inputs.txt;
gamma:2 sv {?[(count x where x="1")>count x where x="0";1;0]}each i;
epsilon: 2 sv {?[(count x where x="0")>count x where x="1";1;0]}each i;
gamma*epsilon

