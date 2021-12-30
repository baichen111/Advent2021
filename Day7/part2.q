\d .day7part2
i:"I"$"," vs first read0 `:part2inputs.txt
nums:i ,/:i
show min sum {ls:-1_x;n:first -1#x;{[x;n] abs[x-n] +sum til abs x-n}[;n]each ls} each nums

exit 0