m:"I"$string read0 `:Part1Inputs.txt
fakem:{(1#x),x,-1#x}each m
s:sum nums:raze {  x where ((x < 2 xprev x) & (x < -2 xprev x)& (x < prev x) & x < next x) & not x=0} each fakem
zeros:count raze {where x=0}each m
show zeros+s+count nums
