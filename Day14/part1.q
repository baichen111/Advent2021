\d .day14
i:read0 `:part1inputs.txt
ls:first i
dic:(2#'2_i)!-1#'2_i
final:{inputs:(2#')[-2_(1_)\[x]];(raze {(1#x),dic[x]}each inputs),-1#x}/[10;ls]
show (max n) - min n:count each group final

exit 0
