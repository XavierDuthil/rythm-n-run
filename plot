#!/usr/bin/gnuplot
set size 1,1 
set terminal png size 1900, 1000
set output "result/record.png"
set ylabel "G"
set xlabel "time (x20ms)"
#plot "result/xRecording" with lines, "result/yRecording" with lines, "result/zRecording" with lines, 
plot "result/recording" with lines
#set output "result/parsedRecord.png"
#plot "result/recording2" with lines