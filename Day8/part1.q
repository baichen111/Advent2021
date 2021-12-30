\d .day8part1
i:(last') "|" vs' read0 `:part1inputs.txt
m:raze {" " vs trim x} each i
show count  where (count each m) in 2 4 3 7

exit 0