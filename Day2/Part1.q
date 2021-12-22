t:flip `dir`distance!("SI";" ") 0: `:Part1Inputs.txt;
t:update neg distance from t where dir=`up;
t1:select sum distance from t where dir in `down`up;
t2:select sum distance from t where dir=`forward;
show t1*t2
