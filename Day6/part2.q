\d .day6part2       / for such a huge value, I iterate dictionary instead of iterating list
i:"I"$"," vs first read0 `:part1inputs.txt
g:count each group i
f:{d:()!();k:key x;
  $[not null x[0];[d[-1+except[k;0]]+:x[except[k;0]];d[6]+:x[0];d[8]+:x[0]];d[-1+k]+:value x];
  d}

s:sum f/[256;g]
show s
exit 0